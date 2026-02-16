import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("models/housing_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

st.title("🏠 Housing Price Prediction App")

st.write("Enter housing details below:")

# Example inputs (basic)
longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")
housing_median_age = st.number_input("Housing Median Age")
total_rooms = st.number_input("Total Rooms")
total_bedrooms = st.number_input("Total Bedrooms")
population = st.number_input("Population")
households = st.number_input("Households")
median_income = st.number_input("Median Income")

# Ocean proximity dropdown
ocean_proximity = st.selectbox(
    "Ocean Proximity",
    ["INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND", "<1H OCEAN"]
)

if st.button("Predict Price"):

    input_data = {
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income
    }

    input_df = pd.DataFrame([input_data])

    # One-hot encoding same as training
    input_df = pd.get_dummies(input_df)

    # Ensure same columns
    for col in feature_columns:
        if col not in input_df:
            input_df[col] = 0

    input_df = input_df[feature_columns]

    prediction = model.predict(input_df)

    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
