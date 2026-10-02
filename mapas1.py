import pandas as pd
import numpy as np
import streamlit as st

map_data = pd.DataFrame(
  np.random.randn(1000, 2) / [50, 50] + [18.90389, -97.02154],
  columns=['lat', 'lon'])

st.title("USBI Ixtac")
st.header("Facultad de Negocios y Tecnologías")

st.map(map_data)