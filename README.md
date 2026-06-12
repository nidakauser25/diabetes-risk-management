# 🩺 Diabetes Risk Management System (AI Powered)

## 🚀 Project Overview
The Diabetes Risk Management System is an AI-powered web application built using Streamlit that predicts whether a person is at high or low risk of diabetes based on medical parameters.  
The system uses a trained Machine Learning model to analyze patient data and provide instant predictions through an interactive dashboard.

---

## 🎯 Features
- 🔐 Secure Login Page (Demo Authentication)
- 🧠 Machine Learning Prediction Model
- 🌑 Dark Theme UI (Black / Grey / White Professional Design)
- 📊 Interactive Streamlit Dashboard
- ⚡ Real-time Prediction System
- 🎈 Animated Result Output (Balloons / Alerts)
- 📱 User-friendly Interface

---

## 🛠 Tech Stack
- Python 🐍
- Streamlit 🎨
- NumPy 🔢
- Joblib 📦
- Scikit-learn 🤖
- Machine Learning (Random Forest Model)

---

## 🧠 How It Works
1. User logs into the system
2. Enters medical parameters:
   - Pregnancies
   - Glucose Level
   - Blood Pressure
   - Skin Thickness
   - Insulin
   - BMI
   - Diabetes Pedigree Function
   - Age
3. AI model processes the inputs
4. System predicts:
   - ✅ Low Risk
   - ⚠ High Risk

---

## 📂 Project Structure
diabetes-risk-management/ │ ├── app.py ├── models/ │   └── diabetes_model.pkl ├── utils/ │   └── preprocessing.py ├── requirements.txt ├── README.md

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/shariqua06/diabetes-risk-management.git
2️⃣ Navigate to Project Folder
Bash
cd diabetes-risk-management
3️⃣ Install Dependencies
Bash
pip install -r requirements.txt
4️⃣ Run the Application
Bash
streamlit run app.py

📦 Requirements

streamlit
numpy
joblib
scikit-learn
pandas

🔐 Login Credentials (Demo)

Username: admin
Password: admin123

👩‍💻 Author Details
Name: Shariqua Tabassum G
Intern ID: CITS3942
Company: Codtech IT Solutions
Internship Duration: 4 Weeks

📌 GitHub Repository
🔗 https://github.com/shariqua06/diabetes-risk-management⁠�

⭐ Outcome
This project demonstrates the application of Machine Learning in healthcare for early diabetes risk detection using a clean and interactive web interface.

🚀 Future Improvements
Add probability-based prediction
Add patient history database
Improve UI with charts and analytics
Deploy on cloud (Streamlit Sharing / Render)

⚠ Disclaimer
This project is for educational purposes only and should not be used as a real medical diagnosis tool.