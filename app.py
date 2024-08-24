from cProfile import label
import streamlit as st
import pandas as pd
st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")
df = pd.read_csv("data.csv")
st.write(df)

from datetime import time

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)
