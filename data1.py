import streamlit as st
import pandas as pd
names_link = "https://raw.githubusercontent.com/softbytavz/FC26dataset/refs/heads/main/FC26_Data.csv"
names_data = pd.read_csv(names_link)

st.tittle("streamlit and pandas")
st.dataframe(names_data)