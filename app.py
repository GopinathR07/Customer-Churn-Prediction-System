import streamlit as st
import pickle
import numpy as np
import os

# Load model
model_path = os.path.join(os.getcwd(), "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure (months)", min_value=0)
monthly = st.number_input("Monthly Charges", min_value=0.0)

if st.button("Predict"):
    input_data = np.array([[tenure, monthly]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.error(f"Customer will churn (Prob: {probability:.2f})")
    else:
        st.success(f"Customer will stay (Prob: {1-probability:.2f})")
