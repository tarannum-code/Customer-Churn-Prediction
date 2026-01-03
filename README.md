# 📉 Telco Customer Churn Prediction

A **production-ready machine learning project** that predicts whether a telecom customer is likely to churn based on demographic, service usage, and billing information.  
The project includes **data analysis notebooks**, a **trained ML model**, and a **deployable application layer**.

For live DEMO: 
https://customer-churn-prediction-i4vr.onrender.com
---

## 🚀 Project Overview

Customer churn is a critical business problem in the telecom industry.  
This project uses **machine learning** to identify customers who are at high risk of leaving the service, enabling proactive retention strategies.

The solution covers:
- Data analysis & preprocessing
- Feature engineering (one-hot encoding)
- Model training & evaluation
- Model persistence
- Application-ready inference

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Classifier  
- **Target Variable:** `Churn`  
- **Model File:** `model.sav`  
- **Framework:** scikit-learn  

The model outputs:
- **Churn prediction:** Yes / No
- **Churn probability**

---

## 📊 Features Used

### Numerical Features
- `SeniorCitizen`
- `MonthlyCharges`
- `TotalCharges`

### Categorical Features (One-Hot Encoded)
- Gender
- Partner
- Dependents
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- Tenure Group

> ⚠️ Feature order and encoding strictly match the training dataset.

---

## 🗂️ Current Project Structure

├── .ipynb_checkpoints/
├── app.py # Application / API logic
├── Churn Prediction Model.ipynb # Model training notebook
├── Teclo Churn Analysis.ipynb # Exploratory data analysis
├── model.sav # Trained ML model
├── tel_churn.csv # Processed dataset
├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Raw dataset


---

## 📓 Notebooks

- **Teclo Churn Analysis.ipynb**
  - Exploratory Data Analysis (EDA)
  - Data cleaning
  - Insights & visualizations

- **Churn Prediction Model.ipynb**
  - Feature engineering
  - Model training
  - Model evaluation
  - Model serialization (`model.sav`)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/telco-churn-prediction.git
cd telco-churn-prediction

2️⃣ Create Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application

If app.py is used for inference or API:

python -m streamlit run app.py

📈 Prediction Output

The model provides:

Churn classification (Yes / No)

Churn probability score

Example:

Prediction: No Churn
Probability: 0.18

🧩 Technologies Used

Python

Pandas

NumPy

scikit-learn

Streamlit / FastAPI (if enabled)

Pickle

🌍 Deployment Ready

This project can be extended and deployed using:

FastAPI

Docker

AWS / Azure / Render

Streamlit Cloud

🔮 Future Enhancements

Production REST API

Advanced UI dashboard

SHAP explainability

Batch predictions

CI/CD pipeline

Cloud deployment

👨‍💻 Author

Your Name
Data Scientist | Machine Learning Engineer

📧 Email: your.email@example.com

🔗 GitHub: https://github.com/your-username

🔗 LinkedIn: https://linkedin.com/in/yourprofile

⭐ Support

If you find this project useful, please consider giving it a ⭐ on GitHub.
