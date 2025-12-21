import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(page_title="Project Data Explorer", layout="wide")

st.title("🚀 Project Data Analysis App")
st.markdown("Directly converted from your Jupyter Notebook project.")

# 1. Data Loading Section
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # 2. Data Preview
    st.subheader("1. Dataset Preview")
    st.dataframe(df.head())
    
    # 3. Quick Stats
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Descriptive Statistics:**")
        st.write(df.describe())
    with col2:
        st.write("**Missing Values:**")
        st.write(df.isnull().sum())

    # 4. Visualizations Section
    st.subheader("2. Visualizations")
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    if numeric_cols:
        target_col = st.selectbox("Select column for Histogram:", numeric_cols)
        
        fig, ax = plt.subplots()
        sns.histplot(df[target_col], kde=True, ax=ax, color='skyblue')
        ax.set_title(f"Distribution of {target_col}")
        st.pyplot(fig)
        
        # Heatmap
        if len(numeric_cols) > 1:
            st.write("**Correlation Heatmap:**")
            fig_corr, ax_corr = plt.subplots(figsize=(10, 6))
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="YlGnBu", ax=ax_corr)
            st.pyplot(fig_corr)
    else:
        st.error("No numeric columns found for plotting.")
else:
    st.info("Waiting for CSV file upload...")