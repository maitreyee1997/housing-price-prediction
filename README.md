# 🏠 Housing Price Prediction App

An end-to-end Machine Learning project that predicts house prices based on various housing features.  
The model is trained using the California Housing dataset and deployed using Streamlit.

---

## 📌 Project Overview

This project predicts the median house value based on:

- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income
- Ocean Proximity

It follows a complete Data Science workflow:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Model Saving
- Web App Deployment

---

## 🧠 Problem Statement

Accurately predicting house prices helps:
- Real estate investors
- Property buyers
- Financial institutions
- Housing analysts

The goal is to build a regression model that predicts `median_house_value`.

---

## ⚙️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit

---

## 📊 Model Used

### 1️⃣ Linear Regression (Baseline Model)

Evaluation Metrics:
- MSE: 4,793,349,395
- RMSE: 69,234
- R² Score: 0.63

---

### 2️⃣ Random Forest Regressor (Final Model)

Evaluation Metrics:
- MSE: 2,371,038,697
- RMSE: 48,693
- R² Score: 0.82

Random Forest performed significantly better and was selected as the final model.

---

## 💾 Model Saving

The trained model is saved using:

```python
joblib.dump(rf_model, "models/housing_model.pkl")
```

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository

```
git clone <your-repo-link>
cd housing_price_prediction
```

### 2️⃣ Create and Activate Virtual Environment

```
conda create -n housing_env python=3.10
conda activate housing_env
```

### 3️⃣ Install Requirements

```
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App

```
streamlit run application.py
```

App will open at:
```
http://localhost:8501
```

---

## 🌐 App Features

- User-friendly input interface
- Dropdown for Ocean Proximity
- Real-time price prediction
- Clean UI using Streamlit
- End-to-end ML deployment

---

## 📂 Project Structure

```
housing_price_prediction/
│
├── data/
├── models/
│   └── housing_model.pkl
├── notebook/
│   └── housing_model_training.ipynb
├── application.py
├── requirements.txt
└── README.md
```

---

## 📈 Future Improvements

- Hyperparameter tuning
- Cross-validation
- Feature importance visualization
- Deployment on Streamlit Cloud
- Docker containerization

---

## 👩‍💻 Author

Maitreyee  
Data Analyst | Aspiring Data Scientist  

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
