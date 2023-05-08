import streamlit as st
import pickle
import numpy as np


def show_predict_page():
    st.title("Instagram Reach Analysis & Prediction")

    categories = ("Food", "Sports", "Music", "Dance", "Photography")
    hours = list(range(24))

    category = st.selectbox("Category", categories)
    hour = st.selectbox("Time of Post", hours)

    followers = st.number_input("No. of Followers", step=1)

    result = followers * 2
    st.write("The result is:", result)

    ok = st.button("Predict Now")