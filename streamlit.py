import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as grid
import os
import sys
import warnings


warnings.filterwarnings("ignore")


@st.cache_data
def load_data():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
    )
    return df


# Page setting
st.set_page_config(layout="wide", page_title="Cars", page_icon=":bar_chart:")

st.markdown(
    "<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True
)

st.title(":bar_chart: Cars")
st.write("Big Data no fun. That's all")

df = load_data()
# Create a text element and let the reader know the data is loading.
data_load_state = st.text("Loading data...")
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done!")


st.sidebar.header("Choose your filter")
region = st.sidebar.multiselect("Pick your Region", df["continent"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["continent"].isin(region)]

st.subheader("Heat map")
# graph here(create maybe a file for graphs?)
numeric_cols = df2.select_dtypes(include=["float64", "int64"])
correlation_matrix = numeric_cols.corr()
viz_correlation = sns.heatmap(
    correlation_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    center=0,
    annot=True,
    fmt=".2f",
    square=True,
    linewidths=0.5,
)

st.pyplot(viz_correlation.figure)

st.subheader("Pair plot")
# graph here
pairData = sns.pairplot(df2)
st.pyplot(pairData.figure)


if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.dataframe(df.head(20))
