import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.pipeline import make_pipeline
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(page_title="Earthquake Damage Classifier", 
                   page_icon="🏠", 
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("🏠 Earthquake Damage Classification - WQU Project 4")
st.markdown("**Predict building damage in Kavrepalanchok district using Logistic Regression & Decision Trees**")

# Sidebar for data loading options
st.sidebar.header("📊 Data Loading")
data_source = st.sidebar.radio("Choose data source:", 
                              ["Load from Kaggle CSV (Recommended)", 
                               "Load from SQLite (if available)", 
                               "Use sample data"])

if data_source == "Load from Kaggle CSV (Recommended)":
    st.sidebar.info("Download from: https://www.kaggle.com/datasets/mullerismail/richters-predictor-modeling-earthquake-damage")
    uploaded_train = st.sidebar.file_uploader("Upload train_values.csv", type='csv')
    uploaded_labels = st.sidebar.file_uploader("Upload train_labels.csv", type='csv')
    
    if uploaded_train and uploaded_labels:
        df_features = pd.read_csv(uploaded_train)
        df_labels = pd.read_csv(uploaded_labels)
        df = df_features.merge(df_labels, on='building_id')
    else:
        st.sidebar.warning("Upload both CSV files to proceed")
        df = None

elif data_source == "Use sample data":
    # Create sample data matching your head
    sample_data = {
        'building_id': [87473, 87479, 87482, 87491, 87496],
        'age_building': [15, 12, 23, 12, 32],
        'plinth_area_sq_ft': [382, 328, 427, 427, 360],
        'height_ft_pre_eq': [18, 7, 20, 14, 18],
        'land_surface_condition': ['Flat']*5,
        'foundation_type': ['Mud mortar-Stone/Brick']*5,
        'roof_type': ['Bamboo/Timber-Light roof']*5,
        'ground_floor_type': ['Mud']*5,
        'other_floor_type': ['TImber/Bamboo-Mud', 'Not applicable', 'TImber/Bamboo-Mud', 'TImber/Bamboo-Mud', 'TImber/Bamboo-Mud'],
        'position': ['Not attached']*5,
        'plan_configuration': ['Rectangular']*5,
        'superstructure': ['Stone, mud mortar']*5,
        'severe_damage': [1, 1, 1, 1, 1]
    }
    df = pd.DataFrame(sample_data)
    
else:
    try:
        # Try to connect to sqlite if available
        conn = sqlite3.connect('nepal.sqlite')
        query = """
        SELECT DISTINCT i.building_id AS bid, 
               s.age_building, s.plinth_area_sq_ft, s.height_ft_pre_eq,
               s.land_surface_condition, s.foundation_type, s.roof_type,
               s.ground_floor_type, s.other_floor_type, s.position,
               s.plan_configuration, s.superstructure,
               CASE WHEN d.damage_grade IN ('Grade 4', 'Grade 5') THEN 1 ELSE 0 END as severe_damage
        FROM id_map AS i 
        JOIN building_structure AS s ON i.building_id = s.building_id 
        JOIN building_damage AS d ON i.building_id = d.building_id
        WHERE i.district_id = 28  -- Kavrepalanchok
        """
        df = pd.read_sql(query, conn, index_col='bid')
        conn.close()
        st.success("✅ SQLite data loaded successfully!")
    except:
        st.error("❌ SQLite file not found. Use CSV or sample data.")
        df = None

if df is not None and not df.empty:
    st.success(f"✅ Data loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")
    
    # Data exploration tab
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Explore Data", "🔄 Preprocess", "🤖 Train Models", "📊 Results"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Dataset Overview")
            st.dataframe(df.head(), use_container_width=True)
            st.metric("Total Buildings", len(df))
            st.metric("Severe Damage Rate", f"{df['severe_damage'].mean():.1%}")
        
        with col2:
            st.subheader("Target Distribution")
            fig_pie = px.pie(df, names='severe_damage', 
                           title="Severe Damage Distribution",
                           color_discrete_map={0: '#4CAF50', 1: '#F44336'})
            st.plotly_chart(fig_pie, use_container_width=True)
            
            st.subheader("Key Features")
            top_features = ['age_building', 'plinth_area_sq_ft', 'height_ft_pre_eq']
            fig_hist = make_subplots(rows=1, cols=3, subplot_titles=top_features)
            for i, feat in enumerate(top_features, 1):
                fig_hist.add_trace(go.Histogram(x=df[feat], name=feat, nbinsx=20), row=1, col=i)
            fig_hist.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_hist, use_container_width=True)
    
    with tab2:
        st.subheader("Preprocessing Pipeline")
        
        # Filter for Kavrepalanchok (district_id=28)
        if 'district_id' in df.columns:
            df_filtered = df[df['district_id'] == 28]
        else:
            df_filtered = df.copy()
        
        # Select features (matching WQU notebook)
        feature_cols = ['age_building', 'plinth_area_sq_ft', 'height_ft_pre_eq',
                       'land_surface_condition', 'foundation_type', 'roof_type',
                       'ground_floor_type', 'other_floor_type', 'position',
                       'plan_configuration', 'superstructure']
        
        # Handle missing values
        df_clean = df_filtered[feature_cols + ['severe_damage']].dropna()
        
        # Encode categorical variables
        le = LabelEncoder()
        for col in feature_cols:
            if df_clean[col].dtype == 'object':
                df_clean[col] = le.fit_transform(df_clean[col].astype(str))
        
        X = df_clean[feature_cols]
        y = df_clean['severe_damage']
        
        st.success(f"✅ Preprocessed: {X.shape[0]} samples, {X.shape[1]} features")
        st.dataframe(X.head(), use_container_width=True)
    
    with tab3:
        if 'X' in locals():
            st.subheader("Model Training")
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                              random_state=42, stratify=y)
            
            # Model selection
            model_choice = st.selectbox("Choose model:", 
                                      ["Logistic Regression", "Decision Tree"])
            
            if model_choice == "Logistic Regression":
                model = make_pipeline(StandardScaler(), LogisticRegression(random_state=42))
            else:
                model = DecisionTreeClassifier(max_depth=5, random_state=42)
            
            if st.button("🚀 Train Model", type="primary"):
                with st.spinner("Training model..."):
                    model.fit(X_train, y_train)
                    train_acc = accuracy_score(y_train, model.predict(X_train))
                    st.success(f"✅ Model trained! Train Accuracy: {train_acc:.3f}")
            
            st.info("Models use the same features and preprocessing as WQU notebook 4.5")
    
    with tab4:
        if 'model' in locals():
            st.subheader("Model Performance")
            
            y_pred = model.predict(X_test)
            y_pred_proba = model.predict_proba(X_test)[:, 1]
            
            # Metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Test Accuracy", f"{accuracy_score(y_test, y_pred):.3f}")
            with col2:
                st.metric("Precision", f"{classification_report(y_test, y_pred, output_dict=True)['1']['precision']:.3f}")
            with col3:
                st.metric("Recall", f"{classification_report(y_test, y_pred, output_dict=True)['1']['recall']:.3f}")
            with col4:
                st.metric("F1-Score", f"{classification_report(y_test, y_pred, output_dict=True)['1']['f1-score']:.3f}")
            
            # Confusion Matrix
            st.subheader("Confusion Matrix")
            cm = confusion_matrix(y_test, y_pred)
            fig_cm = px.imshow(cm, text_auto=True, aspect="auto",
                             labels=dict(x="Predicted", y="Actual", color="Count"),
                             color_continuous_scale='Blues')
            st.plotly_chart(fig_cm, use_container_width=True)
            
            # Feature Importance (for Decision Tree)
            if hasattr(model, 'feature_importances_'):
                st.subheader("Feature Importance")
                importances = pd.DataFrame({
                    'feature': feature_cols,
                    'importance': model.feature_importances_
                }).sort_values('importance', ascending=True)
                
                fig_imp = px.bar(importances, x='importance', y='feature',
                               orientation='h', title="Decision Tree Feature Importance")
                st.plotly_chart(fig_imp, use_container_width=True)
            
            # Classification Report
            st.subheader("Detailed Classification Report")
            st.text(classification_report(y_test, y_pred))
        
        else:
            st.info("👆 Train a model first in the 'Train Models' tab")

else:
    st.warning("⚠️ Please upload data files or use sample data to proceed")
    st.markdown("""
    ## Quick Start Guide:
    1. **Download data** from [Kaggle](https://www.kaggle.com/datasets/mullerismail/richters-predictor-modeling-earthquake-damage)
    2. Upload `train_values.csv` and `train_labels.csv`
    3. Explore → Preprocess → Train → Analyze!
    
    This app replicates **WQU ADSL Project 4** exactly:
    - Kavrepalanchok district (district_id=28)
    - Same features as notebook 4.5
    - Logistic Regression + Decision Tree
    - Full evaluation metrics
    """)

# Footer
st.markdown("---")
st.markdown("*WorldQuant University Applied Data Science Lab - Project 4 (Streamlit App)* [file:62]")
