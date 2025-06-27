import streamlit as st
import numpy as np
import joblib

model = joblib.load("kidney_model_6features.pkl")

st.title("🩺 Kidney Disease Prediction (6 Features)")
st.write("Enter patient data below:")

# Collect only 6 inputs
age = st.number_input("Age", 0.0, 100.0)
bp = st.number_input("Blood Pressure (Diastolic - lower value, e.g., 80)", 0.0)
al = st.number_input("Albumin", 0.0, 5.0, step=0.1)
hemo = st.number_input("Hemoglobin", 0.0)
bgr = st.number_input("Blood Glucose Random", 0.0)
sc = st.number_input("Serum Creatinine", 0.0)

# Create input array
input_data = np.array([[age, bp, al, hemo, bgr, sc]])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ Kidney Disease Detected")
    else:
        st.success("✅ No Kidney Disease")
