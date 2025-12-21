import streamlit as st
import pandas as pd

st.title("Buenos Aires Housing EDA")

uploaded_file = st.file_uploader("Upload the CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
else:
    st.info("Please upload buenos-aires-real-estate-1.csv to start.")
