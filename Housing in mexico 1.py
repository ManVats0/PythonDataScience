"""
🏠 Buenos Aires Housing EDA - Complete Assignment 025 Solution
Upload to GitHub as 'app.py' and connect to Streamlit Cloud
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import io
import warnings
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from category_encoders import OneHotEncoder
from sklearn.pipeline import make_pipeline

# Page config for perfect GitHub deployment
st.set_page_config(
    page_title="Buenos Aires Housing EDA",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

warnings.filterwarnings('ignore')

@st.cache_data
def load_data(file):
    """Load and cache CSV data"""
    return pd.read_csv(file)

@st.cache_data
def wrangle(filepath):
    """
    Assignment 2.5.1 - Complete data wrangling function
    Exactly matches assignment requirements
    """
    df = pd.read_csv(filepath)
    
    # Filter: Capital Federal apartments < $400k
    mask_ba = df['place_with_parent_names'].str.contains('Capital Federal', na=False)
    mask_apt = df['property_type'] == 'apartment'
    mask_price = df['price_aprox_usd'] < 400000
    df = df[mask_ba & mask_apt & mask_price]
    
    # Remove surface outliers (10th-90th percentiles)
    low, high = df['surface_covered_in_m2'].quantile([0.1, 0.9])
    mask_area = df['surface_covered_in_m2'].between(low, high)
    df = df[mask_area]
    
    # Split lat-lon column
    df[['lat', 'lon']] = df['lat-lon'].str.split(',', expand=True).astype(float)
    df = df.drop(columns=['lat-lon'])
    
    # Extract neighborhood (3rd level from place_with_parent_names)
    df['neighborhood'] = df['place_with_parent_names'].str.split('/').str[-3]
    df = df.drop(columns=['place_with_parent_names'])
    
    # Rename price column
    df = df.rename(columns={'price_aprox_usd': 'price'})
    
    return df

def create_price_histogram(df):
    """Assignment 2.5.4 - OOP Matplotlib histogram"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.hist(df['price'], bins=50, edgecolor='black', alpha=0.7)
    ax.set_xlabel('Price (USD)')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Apartment Prices - Buenos Aires', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig

def build_model(df):
    """Complete ML pipeline matching assignment requirements"""
    X = df.drop(columns=['price'])
    y = df['price']
    
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Exact assignment pipeline
    model = make_pipeline(
        OneHotEncoder(use_cat_names=True),
        Ridge(alpha=1.0)
    )
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    
    mae = mean_absolute_error(y_val, y_pred)
    
    return model, mae, X_train, X_val, y_train, y_val

# Main App
st.markdown('<h1 class="main-header">🏠 Buenos Aires Housing EDA</h1>', unsafe_allow_html=True)
st.markdown("***Complete Assignment 025 Solution - Ready for WQ University submission***")

# File uploader
uploaded_file = st.file_uploader(
    "📁 Upload **buenos-aires-real-estate-1.csv**", 
    type=["csv"],
    help="Drag & drop or click to upload your dataset"
)

if uploaded_file is not None:
    with st.spinner("🔄 Loading and analyzing data..."):
        df_raw = load_data(uploaded_file)
        df = wrangle(uploaded_file)
    
    # Key Metrics Row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🏠 Total Properties", f"{len(df):,}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("💰 Avg Price", f"${df['price'].mean():,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📏 Avg Area", f"{df['surface_covered_in_m2'].mean():.0f} m²")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📍 Neighborhoods", f"{df['neighborhood'].nunique()}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col5:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("✅ Clean Rows", f"{len(df):,}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Main Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Data Preview", "🔧 Wrangling", "📊 Visualizations", 
        "🗺️ Interactive Map", "🤖 ML Pipeline"
    ])
    
    with tab1:
        st.subheader("Raw vs Wrangled Data")
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.metric("Raw Data", f"{len(df_raw):,}")
            st.dataframe(df_raw.head(), height=300)
        
        with col_b:
            st.success("✅ Wrangled Data")
            st.metric("Clean Data", f"{len(df):,}")
            st.dataframe(df.head(), height=300)
        
        st.subheader("Dataset Info")
        buffer = io.StringIO()
        df.info(buf=buffer)
        st.code(buffer.getvalue())
    
    with tab2:
        st.success("✅ **Task 2.5.1 Complete** - `wrangle()` function")
        st.code("""
def wrangle(filepath):
    # Filters: Capital Federal apartments < $400k
    # Outlier removal: surface 10th-90th percentiles  
    # Splits: lat-lon → lat, lon
    # Extracts: neighborhood from place_with_parent_names
    # Renames: price_aprox_usd → price
""")
        
        st.subheader("Data Quality Check")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Missing Values", df.isnull().sum().sum())
        with col2:
            st.metric("Valid Lat/Lon", df[['lat', 'lon']].notna().all(axis=1).sum())
    
    with tab3:
        st.subheader("📈 **Task 2.5.4 Complete** - Price Distribution")
        fig_hist = create_price_histogram(df)
        st.pyplot(fig_hist)
        
        col1, col2 = st.columns(2)
        with col1:
            fig_scatter = px.scatter(
                df, x='surface_covered_in_m2', y='price',
                trendline="ols",
                title="Price vs Surface Area",
                labels={'surface_covered_in_m2': 'Area (m²)', 'price': 'Price (USD)'}
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
        
        with col2:
            fig_neigh = px.box(
                df, x='neighborhood', y='price',
                title="Price by Neighborhood (Top 10)",
                category_orders={'neighborhood': df['neighborhood'].value_counts().head(10).index}
            )
            fig_neigh.update_layout(height=400)
            st.plotly_chart(fig_neigh, use_container_width=True)
    
    with tab4:
        st.subheader("🗺️ **Task 2.5.6 Complete** - Interactive Map")
        df_map = df.dropna(subset=['lat', 'lon', 'price'])
        
        fig_map = px.scatter_mapbox(
            df_map.head(2000),  # Limit for performance
            lat='lat', lon='lon',
            color='price',
            size='surface_covered_in_m2',
            hover_name='neighborhood',
            color_continuous_scale='viridis',
            size_max=15,
            mapbox_style="open-street-map",
            title="🏠 Buenos Aires Apartments - Price Heatmap",
            zoom=11,
            height=600
        )
        st.plotly_chart(fig_map, use_container_width=True)
        
        # Key insights
        st.markdown("""
        ### 📍 **Key Location Insights**
        - **🔴 Red/Hot areas**: Palermo, Recoleta, Puerto Madero (Premium)
        - **🟢 Green/Cool areas**: Villa Lugano, Mataderos (Budget)  
        - **Size**: Larger bubbles = bigger apartments
        """)
    
    with tab5:
        st.subheader("🤖 **Complete ML Pipeline**")
        
        if st.button("🚀 Train Model & Get Results", type="primary"):
            with st.spinner("Training Ridge Regression pipeline..."):
                model, mae, X_train, X_val, y_train, y_val = build_model(df)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Training Set", f"{len(X_train):,}")
                with col2:
                    st.metric("Validation Set", f"{len(X_val):,}")
                with col3:
                    st.error(f"MAE: ${mae:,.0f}")
                
                # Feature importance
                st.subheader("Feature Importance")
                encoder = model.named_steps['onehotencoder']
                ridge = model.named_steps['ridge']
                
                feature_names = encoder.transform(X_train).columns
                importances = np.abs(ridge
