import streamlit as st
import pandas as pd

st.title("Cahi Sales Dashboard")
file = st.file_uploader("Upload Your File" , type=["CSV"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Priviwe")
    st.dataframe(df)

if file:
    st.subheader("summary stats")
    st.write(df.describe())

if file:
    cityes = df["City"].unique()
    selected_citys = st.selectbox("filter by cities" , cityes)
    filtered_data = df[df["City"] == selected_citys]
    st.dataframe(filtered_data)