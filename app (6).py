import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure")
monthly = st.number_input("Monthly Charges")

if st.button("Predict"):
    # Assuming the input features for prediction are `tenure` and `monthly_charges`
    # and the model expects features in the same order and scaling as training.
    # In a real application, you'd likely need to preprocess these inputs
    # (e.g., scale them) before passing them to the model.

    # For demonstration, we'll use a placeholder array for full features if the model expects more.
    # This part needs to be adjusted based on the actual model's expected input shape and features.
    # Let's assume for now, the model was trained only on tenure and monthly charges for simplicity
    # or that the input_data needs to be a specific shape that aligns with the model's training.

    # If the model expects only 2 features (tenure, monthly):
    input_data = np.array([[tenure, monthly]])
    
    # If the model expects 19 features (like your X DataFrame):
    # You would need to create a full 19-feature array, filling in defaults or user inputs
    # for all other features (gender, SeniorCitizen, Partner, Dependents, etc.)
    # For this example, let's assume the model is simplified to take only these two inputs
    # or that these inputs are enough to make a prediction by some internal model logic.
    # TODO: This needs careful consideration based on the actual model trained.

    result = model.predict(input_data)

    if result[0] == 1:
        st.error("Customer will churn")
    else:
        st.success("Customer will stay")
