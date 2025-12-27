import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.pipeline import make_pipeline
import seaborn as sns
import matplotlib.pyplot as plt
from google.cloud import bigquery
from google.oauth2 import service_account  # for service-account auth [web:120]
import warnings

warnings.filterwarnings("ignore")

# -------------------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Earthquake Damage Classifier",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🏠 Earthquake Damage Classification App")
st.markdown(
    "**Predict building damage in Kavrepalanchok district using Logistic Regression & Decision Trees**"
)

# -------------------------------------------------------------------
# SIDEBAR: DATA SOURCE
# -------------------------------------------------------------------
st.sidebar.header("📊 Data Loading")
data_source = st.sidebar.radio(
    "Choose data source:",
    ["Load from Kaggle CSV (Recommended)", "Load from BigQuery", "Use sample data"],
)

# -------------------------------------------------------------------
# 1. LOAD DATA
# -------------------------------------------------------------------
df = None

if data_source == "Load from Kaggle CSV (Recommended)":
    st.sidebar.info(
        "Download from: https://www.kaggle.com/datasets/mullerismail/richters-predictor-modeling-earthquake-damage"
    )
    uploaded_train = st.sidebar.file_uploader("Upload train_values.csv", type="csv")
    uploaded_labels = st.sidebar.file_uploader("Upload train_labels.csv", type="csv")

    if uploaded_train is not None and uploaded_labels is not None:
        df_features = pd.read_csv(uploaded_train)
        df_labels = pd.read_csv(uploaded_labels)

        # Merge on building_id
        if "building_id" not in df_features.columns or "building_id" not in df_labels.columns:
            st.error("Both CSVs must contain a 'building_id' column.")
            df = None
        else:
            df = df_features.merge(df_labels, on="building_id")

            # Kaggle: damage_grade in {1,2,3} (3 = most severe)
            if "damage_grade" in df.columns:
                df["severe_damage"] = (df["damage_grade"] == 3).astype(int)
            elif "severe_damage" not in df.columns:
                st.error(
                    "Label file must contain damage_grade or severe_damage column. "
                    "Check that you uploaded the correct train_labels.csv."
                )
                df = None
    else:
        st.sidebar.warning("Upload both CSV files to proceed")
        df = None

elif data_source == "Use sample data":
    sample_data = {
        "building_id": [87473, 87479, 87482, 87491, 87496],
        "age_building": [15, 12, 23, 12, 32],
        "plinth_area_sq_ft": [382, 328, 427, 427, 360],
        "height_ft_pre_eq": [18, 7, 20, 14, 18],
        "land_surface_condition": ["Flat"] * 5,
        "foundation_type": ["Mud mortar-Stone/Brick"] * 5,
        "roof_type": ["Bamboo/Timber-Light roof"] * 5,
        "ground_floor_type": ["Mud"] * 5,
        "other_floor_type": [
            "TImber/Bamboo-Mud",
            "Not applicable",
            "TImber/Bamboo-Mud",
            "TImber/Bamboo-Mud",
            "TImber/Bamboo-Mud",
        ],
        "position": ["Not attached"] * 5,
        "plan_configuration": ["Rectangular"] * 5,
        "superstructure": ["Stone, mud mortar"] * 5,
        "severe_damage": [1, 1, 1, 1, 1],
    }
    df = pd.DataFrame(sample_data)

else:  # Load from BigQuery with service-account credentials
    st.sidebar.info("Reading data from BigQuery table filtered to district_id = 12")

    project_id = "aman-trial-432613"
    dataset_table = "123.nepal"

    sql = f"""
    SELECT
      building_id AS bid,
      age_building,
      plinth_area_sq_ft,
      height_ft_pre_eq,
      land_surface_condition,
      foundation_type,
      roof_type,
      ground_floor_type,
      other_floor_type,
      position,
      plan_configuration,
      superstructure,
      damage_grade,
      district_id
    FROM `{project_id}.{dataset_table}`
    WHERE district_id = 12
    """

    try:
        # Build credentials from Streamlit secrets
        service_account_info = st.secrets["gcp_service_account"]
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

        client = bigquery.Client(
            project=project_id,
            credentials=credentials,
        )

        query_job = client.query(sql)
        df = query_job.to_dataframe(create_bqstorage_client=False)  # [web:79]

        if "damage_grade" in df.columns:
            df["severe_damage"] = (df["damage_grade"] == 3).astype(int)

        df.set_index("bid", inplace=True)
        st.success("✅ BigQuery data loaded successfully!")
    except Exception as e:
        st.error(f"❌ BigQuery load failed: {e}")
        df = None

# -------------------------------------------------------------------
# 2. IF DATA LOADED, SHOW TABS
# -------------------------------------------------------------------
if df is not None and not df.empty:
    st.success(f"✅ Data loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📈 Explore Data", "🔄 Preprocess", "🤖 Train Models", "📊 Results"]
    )

    # ========== TAB 1: EXPLORE ==========
    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Dataset Overview")
            st.dataframe(df.head(), use_container_width=True)
            st.metric("Total Buildings", len(df))
            if "severe_damage" in df.columns:
                st.metric("Severe Damage Rate", f"{df['severe_damage'].mean():.1%}")
            else:
                st.warning("Column 'severe_damage' not found. Check label processing.")

        with col2:
            if "severe_damage" in df.columns:
                st.subheader("Target Distribution")
                fig_pie = px.pie(
                    df,
                    names="severe_damage",
                    title="Severe Damage Distribution",
                    color_discrete_map={0: "#4CAF50", 1: "#F44336"},
                )
                st.plotly_chart(fig_pie, use_container_width=True)

            st.subheader("Key Features")
            top_features = ["age_building", "plinth_area_sq_ft", "height_ft_pre_eq"]
            available_feats = [f for f in top_features if f in df.columns]
            if available_feats:
                fig_hist = make_subplots(
                    rows=1, cols=len(available_feats), subplot_titles=available_feats
                )
                for i, feat in enumerate(available_feats, 1):
                    fig_hist.add_trace(
                        go.Histogram(x=df[feat], name=feat, nbinsx=20), row=1, col=i
                    )
                fig_hist.update_layout(height=400, showlegend=False)
                st.plotly_chart(fig_hist, use_container_width=True)
            else:
                st.info("Key numeric features not found in dataframe.")

    # ========== TAB 2: PREPROCESS ==========
    with tab2:
        st.subheader("Preprocessing Pipeline")

        if "district_id" in df.columns:
            df_filtered = df[df["district_id"] == 12]
        else:
            df_filtered = df.copy()

        feature_cols = [
            "age_building",
            "plinth_area_sq_ft",
            "height_ft_pre_eq",
            "land_surface_condition",
            "foundation_type",
            "roof_type",
            "ground_floor_type",
            "other_floor_type",
            "position",
            "plan_configuration",
            "superstructure",
        ]

        existing_features = [c for c in feature_cols if c in df_filtered.columns]

        if "severe_damage" not in df_filtered.columns:
            st.error(
                "Column 'severe_damage' is missing after loading. "
                "Check that damage_grade was converted correctly."
            )
        else:
            df_clean = df_filtered[existing_features + ["severe_damage"]].dropna()

            le = LabelEncoder()
            for col in existing_features:
                if df_clean[col].dtype == "object":
                    df_clean[col] = le.fit_transform(df_clean[col].astype(str))

            X = df_clean[existing_features]
            y = df_clean["severe_damage"]

            st.success(f"✅ Preprocessed: {X.shape[0]} samples, {X.shape[1]} features")
            st.dataframe(X.head(), use_container_width=True)

    # ========== TAB 3: TRAIN MODELS ==========
    with tab3:
        if "X" in locals() and "y" in locals():
            st.subheader("Model Training")

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )

            model_choice = st.selectbox(
                "Choose model:", ["Logistic Regression", "Decision Tree"]
            )

            if model_choice == "Logistic Regression":
                model = make_pipeline(
                    StandardScaler(), LogisticRegression(random_state=42)
                )
            else:
                model = DecisionTreeClassifier(max_depth=5, random_state=42)

            if st.button("🚀 Train Model", type="primary"):
                with st.spinner("Training model..."):
                    model.fit(X_train, y_train)
                    train_acc = accuracy_score(y_train, model.predict(X_train))
                    st.success(f"✅ Model trained! Train Accuracy: {train_acc:.3f}")

            st.info("Models use the same features and preprocessing as WQU notebook 4.5")
        else:
            st.warning("Go to the 'Preprocess' tab first to prepare X and y.")

    # ========== TAB 4: RESULTS ==========
    with tab4:
        if "model" in locals() and "X_test" in locals() and "y_test" in locals():
            try:
                st.subheader("Model Performance")

                y_pred = model.predict(X_test)
                y_pred_proba = (
                    model.predict_proba(X_test)[:, 1]
                    if hasattr(model, "predict_proba")
                    else None
                )

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Test Accuracy", f"{accuracy_score(y_test, y_pred):.3f}")

                report = classification_report(
                    y_test, y_pred, output_dict=True, zero_division=0
                )
                with col2:
                    st.metric("Precision", f"{report['1']['precision']:.3f}")
                with col3:
                    st.metric("Recall", f"{report['1']['recall']:.3f}")
                with col4:
                    st.metric("F1-Score", f"{report['1']['f1-score']:.3f}")

                st.subheader("Confusion Matrix")
                cm = confusion_matrix(y_test, y_pred)
                fig_cm = px.imshow(
                    cm,
                    text_auto=True,
                    aspect="auto",
                    labels=dict(x="Predicted", y="Actual", color="Count"),
                    color_continuous_scale="Blues",
                )
                st.plotly_chart(fig_cm, use_container_width=True)

                if hasattr(model, "feature_importances_"):
                    st.subheader("Feature Importance")
                    importances = pd.DataFrame(
                        {"feature": existing_features, "importance": model.feature_importances_}
                    ).sort_values("importance", ascending=True)

                    fig_imp = px.bar(
                        importances,
                        x="importance",
                        y="feature",
                        orientation="h",
                        title="Decision Tree Feature Importance",
                    )
                    st.plotly_chart(fig_imp, use_container_width=True)

                st.subheader("Detailed Classification Report")
                st.text(classification_report(y_test, y_pred, zero_division=0))
            except Exception:
                st.error(
                    "Model not trained yet in this session. "
                    "Go to 'Train Models' and click '🚀 Train Model'."
                )
        else:
            st.info("👆 Train a model first in the 'Train Models' tab.")

else:
    st.warning("⚠️ Please upload data files or use BigQuery/sample data to proceed")
    st.markdown(
        """
    ## Quick Start Guide:
    1. **Download data** from [Kaggle](https://www.kaggle.com/datasets/mullerismail/richters-predictor-modeling-earthquake-damage)
    2. Upload `train_values.csv` and `train_labels.csv` or choose **Load from BigQuery**
    3. Explore → Preprocess → Train → Analyze!

    This app replicates **WQU ADSL Project 4**:
    - Kavrepalanchok district (district_id=12 in BigQuery)
    - Same features as notebook 4.5
    - Logistic Regression + Decision Tree
    - Full evaluation metrics
    """
    )
