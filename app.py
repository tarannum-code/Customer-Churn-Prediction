import streamlit as st
import numpy as np
import pickle

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ LOAD MODEL ------------------
with open("model.sav", "rb") as f:
    model = pickle.load(f)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.big-title {
    font-size: 36px;
    font-weight: 700;
}
.sub-title {
    color: #6c757d;
    font-size: 16px;
}
.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="big-title">📉 Customer Churn Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Predict whether a customer is likely to churn using machine learning</div>', unsafe_allow_html=True)
st.markdown("---")

# ------------------ INPUT SECTIONS ------------------
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 👤 Customer Profile")
        name=st.text_input("Customer Name")
        gender = st.radio("Gender", ["Male", "Female"])
        SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
        Partner = st.radio("Partner", ["Yes", "No"])
        Dependents = st.radio("Dependents", ["Yes", "No"])

    with col2:
        st.markdown("### 📞 Services")
        PhoneService = st.radio("Phone Service", ["Yes", "No"])
        MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
        InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

    with col3:
        st.markdown("### 💳 Billing")
        MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=0.0)
        TotalCharges = st.number_input("Total Charges ($)", min_value=0.0)
        PaperlessBilling = st.radio("Paperless Billing", ["Yes", "No"])
        PaymentMethod = st.selectbox(
            "Payment Method",
            [
                "Bank transfer (automatic)",
                "Credit card (automatic)",
                "Electronic check",
                "Mailed check"
            ]
        )

st.markdown("---")

# ------------------ INTERNET ADD-ONS ------------------
st.markdown("### 🌐 Internet Add-on Services")
col4, col5, col6 = st.columns(3)

with col4:
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])

with col5:
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

with col6:
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

st.markdown("---")

# ------------------ TENURE ------------------
st.markdown("### ⏳ Customer Tenure")
tenure_group = st.selectbox(
    "Tenure Group (Months)",
    ["1 - 12", "13 - 24", "25 - 36", "37 - 48", "49 - 60", "61 - 72"]
)

# ------------------ ENCODING ------------------
def encode(value, options):
    return [1 if value == opt else 0 for opt in options]

features = []
features.extend([SeniorCitizen, MonthlyCharges, TotalCharges])
features.extend(encode(gender, ["Female", "Male"]))
features.extend(encode(Partner, ["No", "Yes"]))
features.extend(encode(Dependents, ["No", "Yes"]))
features.extend(encode(PhoneService, ["No", "Yes"]))
features.extend(encode(MultipleLines, ["No", "No phone service", "Yes"]))
features.extend(encode(InternetService, ["DSL", "Fiber optic", "No"]))
features.extend(encode(OnlineSecurity, ["No", "No internet service", "Yes"]))
features.extend(encode(OnlineBackup, ["No", "No internet service", "Yes"]))
features.extend(encode(DeviceProtection, ["No", "No internet service", "Yes"]))
features.extend(encode(TechSupport, ["No", "No internet service", "Yes"]))
features.extend(encode(StreamingTV, ["No", "No internet service", "Yes"]))
features.extend(encode(StreamingMovies, ["No", "No internet service", "Yes"]))
features.extend(encode(Contract, ["Month-to-month", "One year", "Two year"]))
features.extend(encode(PaperlessBilling, ["No", "Yes"]))
features.extend(
    encode(
        PaymentMethod,
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )
)
features.extend(
    encode(
        tenure_group,
        ["1 - 12", "13 - 24", "25 - 36", "37 - 48", "49 - 60", "61 - 72"]
    )
)

# ------------------ PREDICTION ------------------
st.markdown("---")
if st.button("🚀 Predict Churn", use_container_width=True):
    X = np.array(features).reshape(1, -1)
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    st.markdown("## 🔍 Prediction Result")

    st.progress(int(probability * 100))

    if prediction == 1:
        st.error(f"⚠️ **High Risk of {name} to Churn**\n\nProbability: **{probability:.2%}**")
    else:
        st.success(f"✅ **Low Risk of {name} to Churn**\n\nProbability: **{probability:.2%}**")

st.markdown("---")
st.caption("© 2026 • Customer Analytics Platform")