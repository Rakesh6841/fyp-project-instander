import streamlit as st
import pickle
import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MaxAbsScaler
from sklearn.compose import ColumnTransformer

def load_model():
    with open('saved_model.pkl', 'rb') as file:
      data = pickle.load(file)
    return data

data = load_model()

model_loaded = data["model"]
ct_loaded = data["ct"]
scaler_loaded = data["scaler"]

def show_predict_page():
    st.title("Instagram Reach Analysis & Prediction")
    categories = ("food", "photography", "dance", "sports")
    hours = list(range(24))
    category = st.selectbox("Category", categories)
    hour = st.selectbox("Time of Post", hours)
    follower = st.number_input("No. of Followers", step=1)
    post = st.number_input("No. of Posts", step=1)
    predicted_likes = load_model().predict(ct_loaded.transform([[category, hour, follower, post]]))
    ok = st.button("Predict Now")
    if ok:
      st.subheader("The predicted likes : {:.6f}".format(predicted_likes))