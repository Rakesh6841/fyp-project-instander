import streamlit as st
from predict_page import show_predict_page

st.sidebar.selectbox("Predict or Explore", ("Predict", "Explore"))

show_predict_page()