import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")
st.set_page_config(page_title="Housing EDA (Multiple Files)", layout="wide")

st.title("🏠 Housing EDA (Multiple Files Supported)")
st.write("Upload one or more CSV files. The app will combine them and run the same data science steps.")

# -------- 1. MULTI FILE UPLOAD --------
uploaded_files = st.file_uploader(
    "Upload one or more housing CSV files",
    type=["csv"],
    accept_multiple_files=True
)

@st.cache_data
def wrangle_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Clean a DataFrame that is already loaded (no read_csv here)."""

    # 1) price filter and rename
    if "price_aprox_usd" in df.columns:
        df = df[df["price_aprox_usd"].notna()]
        df = df[df["price_aprox_usd"] < 400000]
        df = df.rename(columns={"price_aprox_usd": "price"})
    elif "price" in df.columns:
        df = df[df["price"].notna()]
        df = df[df["price"] < 400000]

    # 2) only apartments if column exists
    if "property_type" in df.columns:
        df = df[df["property_type"] == "apartment"]

    # 3) remove area outliers
    if "surface_covered_in_m2" in df.columns:
        q10, q90 = df["surface_covered_in_m2"].quantile([0.10, 0.90])
        df = df[df["surface_covered_in_m2"].between(q10, q90)]

    # 4) split lat-lon
    if "lat-lon" in df.columns:
        lat_lon_split = df["lat-lon"].str.split(",", expand=True)
        if lat_lon_split.shape[1] >= 2:
            df["lat"] = pd.to_numeric(lat_lon_split[0], errors="coerce")
            df["lon"] = pd.to_numeric(lat_lon_split[1], errors="coerce")
        df = df.drop(columns=["lat-lon"])

    # 5) neighborhood from place_with_parent_names
    if "place_with_parent_names" in df.columns:
        def last_non_empty(s):
            if not isinstance(s, str):
                return np.nan
            parts = [p.strip() for p in s.split("|") if p.strip() != ""]
            return parts[-1] if parts else np.nan

        df["neighborhood"] = df["place_with_parent_names"].apply(last_non_empty)
        df = df.drop(columns=["place_with_parent_names"])

    return df


def plot_price_histogram(df: pd.DataFrame):
    if "price" not in df.columns:
        st.info("No 'price' column found.")
        return
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(df["price"], bins=40, edgecolor="black", alpha=0.7)
    ax.set_xlabel("Price (USD)")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Apartment Prices")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)


# -------- 2. MAIN APP LOGIC --------
if uploaded_files:
    dfs = []
    for f in uploaded_files:
        try:
            df_temp = pd.read_csv(f)  # only place we use read_csv
            df_temp["__source_file"] = f.name
            dfs.append(df_temp)
        except pd.errors.EmptyDataError:
            st.error(f"File '{f.name}' is empty or invalid, skipping.")
        except Exception as e:
            st.error(f"Error reading '{f.name}': {e}")

    if not dfs:
        st.error("No valid CSV files loaded.")
    else:
        df_raw = pd.concat(dfs, ignore_index=True)
        df_clean = wrangle_dataframe(df_raw)

        # NEW: make all column names unique to avoid ValueError
        df_clean = df_clean.loc[:, ~df_clean.columns.duplicated()].copy()

        st.subheader("Clean data preview")
        st.dataframe(df_clean.head())

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Total properties", f"{len(df_clean):,}")
        with c2:
            if "price" in df_clean.columns:
                st.metric("Average price", f"${df_clean['price'].mean():,.0f}")
        with c3:
            if "surface_covered_in_m2" in df_clean.columns:
                st.metric("Average area (m²)", f"{df_clean['surface_covered_in_m2'].mean():.0f}")

        st.subheader("Price distribution")
        plot_price_histogram(df_clean)

        st.subheader("Numeric summary")
        st.dataframe(df_clean.describe())

        if "neighborhood" in df_clean.columns:
            st.subheader("Top neighborhoods by count")
            st.dataframe(df_clean["neighborhood"].value_counts().head(10))

        csv_clean = df_clean.to_csv(index=False)
        st.download_button(
            "💾 Download combined & cleaned CSV",
            csv_clean,
            "housing_cleaned_all_files.csv",
            mime="text/csv"
        )
else:
    st.info("👆 Upload one or more CSV files to start.")


