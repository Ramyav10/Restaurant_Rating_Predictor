import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load everything
model = joblib.load("restaurant_rating_model1.pkl")
encoders = joblib.load("encoders1.pkl")
columns = joblib.load("model_columns1.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Restaurant Rating Predictor")
st.write("Fill in the restaurant details to get the predicted rating.")

# Input fields
city = st.selectbox("City", encoders["City"].classes_)
locality = st.selectbox("Locality", encoders["Locality"].classes_)
cuisines = st.selectbox("Cuisines", encoders["Cuisines"].classes_)
currency = st.selectbox("Currency", encoders["Currency"].classes_)
rating_color = st.selectbox("Rating Color", encoders["Rating color"].classes_)
rating_text = st.selectbox("Rating Text", encoders["Rating text"].classes_)
has_table_booking = st.selectbox("Has Table Booking", ["Yes", "No"])
has_online_delivery = st.selectbox("Has Online Delivery", ["Yes", "No"])
is_delivering_now = st.selectbox("Is Delivering Now", ["Yes", "No"])
switch_to_order_menu = st.selectbox("Switch to Order Menu", ["Yes", "No"])

average_cost = st.number_input("Average Cost for Two", value=500)
price_range = st.slider("Price Range (1-4)", min_value=1, max_value=4, value=2)
longitude = st.number_input("Longitude", value=77.5)
latitude = st.number_input("Latitude", value=12.9)
votes = st.number_input("Votes", value=100)

input_data = pd.DataFrame([[None]*len(columns)], columns=columns)

input_data["City"] = encoders["City"].transform([city])[0]
input_data["Locality"] = encoders["Locality"].transform([locality])[0]
input_data["Cuisines"] = encoders["Cuisines"].transform([cuisines])[0]
input_data["Currency"] = encoders["Currency"].transform([currency])[0]
input_data["Rating color"] = encoders["Rating color"].transform([rating_color])[0]
input_data["Rating text"] = encoders["Rating text"].transform([rating_text])[0]

input_data["Has Table booking"] = 1 if has_table_booking == "Yes" else 0
input_data["Has Online delivery"] = 1 if has_online_delivery == "Yes" else 0
input_data["Is delivering now"] = 1 if is_delivering_now == "Yes" else 0
input_data["Switch to order menu"] = 1 if switch_to_order_menu == "Yes" else 0

input_data["Average Cost for two"] = average_cost
input_data["Price range"] = price_range
input_data["Longitude"] = longitude
input_data["Latitude"] = latitude
input_data["Votes"] = votes
input_data = input_data[columns]
numeric_cols = ["Average Cost for two", "Price range", "Longitude", "Latitude", "Votes"]
input_data[numeric_cols] = scaler.transform(input_data[numeric_cols])

if st.button("Predict Rating"):
    prediction = model.predict(input_data)[0]
    prediction = round(max(0, min(5, prediction)), 2)  # Clamp to 0–5
    st.success(f"Predicted Rating: {prediction}")