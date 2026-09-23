import streamlit as st
import requests
API_URL = "http://127.0.0.1:8000/predict"
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)
st.title("📊 Customer Churn Prediction")
st.write(
    "Enter customer information to predict whether the customer is likely to churn."
)
# -----------------------------
# Customer Information
# -----------------------------
st.header("Customer Information")
col1, col2, col3 = st.columns(3)
with col1:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )
    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )
    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )
    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )
    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=72,
        value=12
    )
with col2:
    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )
    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )
    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )
    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )
    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )
with col3:
    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )
    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )
    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )
    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )
# -----------------------------
# Charges
# -----------------------------
st.header("Billing Information")
col1, col2 = st.columns(2)
with col1:
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=75.5
    )

with col2:

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=900.0
    )
# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Churn"):
    customer_data = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }
    try:
        response = requests.post(
            API_URL,
            json=customer_data
        )
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            probability = result["churn_probability"]
            st.divider()
            if prediction == "Churn":
                st.error(
                    f"⚠️ Customer likely to churn"
                )

            else:

                st.success(
                    f"✅ Customer likely to stay"
                )

            st.metric(
                "Churn Probability",
                f"{probability * 100:.2f}%"
            )
        else:
            st.error(
                f"API Error: {response.status_code}"
            )
    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to FastAPI. "
            "Make sure the FastAPI server is running."
        )