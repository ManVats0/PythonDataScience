import streamlit as st
import pandas as pd
import numpy as np
import warnings

st.set_page_config(page_title="Housing EDA", layout="wide")
warnings.filterwarnings('ignore')

@st.cache_data
def wrangle(file):
    df = pd.read_csv(file)
    if 'price_aprox_usd' in df.columns:
        df = df[df['price_aprox_usd'] < 400000]
    if 'property_type' in df.columns:
        df = df[df['property_type'] == 'apartment']
    if 'surface_covered_in_m2' in df.columns:
        low, high = df['surface_covered_in_m2'].quantile([0.1, 0.9])
        df = df[df['surface_covered_in_m2'].between(low, high)]
    if 'price_aprox_usd' in df.columns:
        df = df.rename(columns={'price_aprox_usd': 'price'})
    return df

st.title("🏠 Buenos Aires Housing EDA")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    df = wrangle(uploaded_file)
    st.success(f"✅ {len(df):,} clean records loaded!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🏠 Properties", len(df))
    with col2:
        st.metric("💰 Avg Price", f"${df['price'].mean():,.0f}")
    
    st.dataframe(df.head())
    st.download_button("💾 Download Clean", df.to_csv(), "clean.csv")
else:
    st.info("👆 Upload CSV to start!")
