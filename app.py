import streamlit as st
import pandas as pd
st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")
df = pd.read_csv("my_data.csv")
st.line_chart(df)