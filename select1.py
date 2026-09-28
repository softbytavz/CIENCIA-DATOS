import streamlit as st
import pandas as pd
st.title("Titanic")

data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(data)
selected_sex = st.selectbox("Select sex", data['sex'].unique())

st.write(f"Selected option: {selected_sex!r}")
filtered_data_sex = data[data['sex'] == selected_sex]

st.dataframe(filtered_data_sex)