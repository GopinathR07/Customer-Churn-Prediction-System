# 📊 Customer Churn Prediction App

A Machine Learning web application that predicts whether a telecom customer is likely to **churn (leave the service)** or **stay**, based on customer data.


## 🚀 Project Overview

Customer churn is a critical problem for subscription-based businesses. This project uses a **Logistic Regression model** to analyze customer behavior and predict churn probability.

The model is deployed using **Streamlit**, allowing users to interactively input customer details and get real-time predictions.


## 🧠 Machine Learning Workflow

1. Data Collection (Telco Customer Dataset)
2. Data Cleaning & Preprocessing
3. Feature Encoding
4. Feature Scaling using StandardScaler
5. Model Training (Logistic Regression)
6. Model Evaluation
7. Deployment using Streamlit


## 📁 Project Structure

```
churn-prediction/
│
├── app.py              # Streamlit web app
├── model.pkl           # Trained ML model
├── scaler.pkl          # Scaler for input data
├── requirements.txt    # Dependencies
├── notebook.ipynb      # Development notebook
├── README.md           # Project documentation
└── .gitignore
```


## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/churn-prediction.git
cd churn-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```


## 🖥️ Usage

* Enter customer details such as:

  * Tenure
  * Monthly Charges
  * (Other features if implemented)
* Click **Predict**
* The app will display:

  * ✅ Customer will stay
  * ❌ Customer will churn


## 📊 Model Details

* **Algorithm:** Logistic Regression
* **Preprocessing:** Label Encoding + Standard Scaling
* **Evaluation Metrics:**

  * Accuracy
  * Precision
  * Recall
  * F1-score


## ⚠️ Limitations

* Current UI may use limited input features
* Label Encoding may introduce ordinal bias
* Model performance depends on data quality


## 🔥 Future Improvements

* Use One-Hot Encoding instead of Label Encoding
* Add full feature inputs in UI
* Display churn probability (%)
* Improve model using advanced algorithms (Random Forest, XGBoost)
* Deploy with public URL


## 🌐 Deployment

You can deploy this app using:

* Streamlit Cloud
* Render
* Hugging Face Spaces


## 👨‍💻 Author

**Gopinath R**


## ⭐ If you found this useful

Give this repository a ⭐ on GitHub!
