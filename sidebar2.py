import streamlit as st
import datetime

# Give user the current date
today = datetime.date.today()
today_date = st.date_input('Current date', today)
st.success('Current date: `%s`' % (today_date))

import pandas as pd
titanic_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
 
# Display the content of the dataset if checkbox is true
st.header("Dataset")
agree = st.checkbox("Mostrar los datos ? ")

if agree:
  st.dataframe(titanic_data)