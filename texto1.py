import streamlit as st

myname = st.text_input('nombre :')
if (myname):
  st.write("tu nombre es : {myname}")