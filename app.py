
import streamlit as st
import joblib
import pandas as pd
import os

# Defining the exact path to your model in Drive
model_path = '/content/drive/MyDrive/Credit_Risk_Engine/credit_risk_model.pkl'

st.title("Bank Loan Risk Engine")

# 1. Loading the model
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file not found!")
    st.stop()

# 2. User Inputs
age = st.number_input("Age", min_value=18, max_value=100)
income = st.number_input("Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)

# 3. Prediction
if st.button("Predict Risk"):
    data = pd.DataFrame([[age, income, loan_amount]], 
                        columns=['Age', 'Income', 'LoanAmount'])
    prediction = model.predict(data)
    
    if prediction[0] == 1:
        st.error("Status: High Risk / Denied")
    else:
        st.success("Status: Approved")
