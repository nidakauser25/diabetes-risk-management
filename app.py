import streamlit as st
import numpy as np
import joblib
import time

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Diabetes AI System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# THEME (White / Grey / Black + Teal Accent)
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #f5f5f5;
    color: #111111;
    font-family: 'Arial';
}

/* Login card */
.login-card {
    background: #ffffff;
    padding: 35px;
    border-radius: 12px;
    width: 400px;
    margin: auto;
    margin-top: 100px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    border: 1px solid #dddddd;
}

/* Inputs */
input {
    background-color: #fafafa !important;
    color: black !important;
    border: 1px solid #cccccc !important;
    border-radius: 8px !important;
    padding: 8px !important;
}

/* Buttons */
div.stButton > button {
    background: #222222;
    color: white;
    border-radius: 6px;
    padding: 10px;
    font-weight: bold;
    transition: 0.3s;
}
div.stButton > button:hover {
    background: #00bcd4;
    color: #ffffff;
    transform: scale(1.02);
}

/* Headings with accent */
h1, h2, h3 {
    color: #111111;
    font-weight: 600;
    border-left: 4px solid #00bcd4;
    padding-left: 8px;
}

/* Cards */
.card {
    background: #ffffff;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

/* Divider */
hr {
    border: 1px solid #dddddd;
}

/* Hide phantom empty boxes created by Streamlit */
div:empty {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD MODEL
# =========================
model = joblib.load("models/diabetes_model.pkl")

def predict(features):
    return model.predict(np.array(features).reshape(1, -1))[0]

# =========================
# SESSION STATE
# =========================
if "login" not in st.session_state:
    st.session_state.login = False

# =========================
# LOGIN PAGE
# =========================
def login_page():
    st.markdown("<h1 style='text-align:center;'>🩺 Diabetes AI System</h1>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)
        st.markdown("### 🔐 Secure Login")

        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login", key="login_btn"):
            if username == "admin" and password == "admin123":
                st.session_state.login = True
                st.success("Login Successful 🚀 Redirecting...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Credentials")

        # Show demo credentials clearly
        st.info("Demo Login → **admin / admin123**")

        st.markdown("</div>", unsafe_allow_html=True)

# =========================
# DASHBOARD
# =========================
def dashboard():
    st.title("🧠 Diabetes Risk Prediction Dashboard")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input("Pregnancies", min_value=0)
        glucose = st.number_input("Glucose Level")
        bp = st.number_input("Blood Pressure")
        skin = st.number_input("Skin Thickness")

    with col2:
        insulin = st.number_input("Insulin")
        bmi = st.number_input("BMI")
        dpf = st.number_input("Diabetes Pedigree Function")
        age = st.number_input("Age")

    st.markdown("---")

    if st.button("🔍 Predict Risk"):
        features = [pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]

        # Validation: prevent all-zero input
        if all(v == 0 for v in features):
            st.warning("⚠ Please enter valid medical values. All zeros are not realistic.")
        else:
            with st.spinner("Running AI model..."):
                time.sleep(2)
            result = predict(features)

            st.markdown("### Result:")
            if result == 1:
                st.error("⚠ HIGH RISK DETECTED")
                st.markdown("Please consult a doctor immediately.")
            else:
                st.success("✅ LOW RISK DETECTED")
                st.markdown("Maintain a healthy lifestyle.")

    st.markdown("---")
    # Logout button
    if st.button("🚪 Logout"):
        st.session_state.login = False
        st.success("You have been logged out.")
        time.sleep(1)
        st.rerun()

# =========================
# MAIN CONTROLLER
# =========================
if not st.session_state.login:
    login_page()
else:
    dashboard()
