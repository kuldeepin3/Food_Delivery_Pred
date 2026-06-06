import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("delivery_model.pkl", "rb"))

# Title
st.title("🚚 Delivery Time Predictor")

st.write("Enter delivery details below:")

# Inputs
distance = st.number_input(
    "Distance (km)",
    min_value=0.0,
    value=5.0
)

prep_time = st.number_input(
    "Preparation Time (minutes)",
    min_value=0.0,
    value=15.0
)

experience = st.number_input(
    "Courier Experience (years)",
    min_value=0.0,
    value=2.0
)

weather = st.selectbox(
    "Weather",
    ["Clear", "Foggy", "Rainy", "Snowy", "Windy"]
)

traffic = st.selectbox(
    "Traffic Level",
    ["High", "Low", "Medium"]
)

time_of_day = st.selectbox(
    "Time of Day",
    ["Afternoon", "Evening", "Morning", "Night"]
)

vehicle = st.selectbox(
    "Vehicle Type",
    ["Bike", "Car", "Scooter"]
)

# Prediction Button
if st.button("Predict Delivery Time"):

    input_df = pd.DataFrame({
        "Distance_km": [distance],
        "Preparation_Time_min": [prep_time],
        "Courier_Experience_yrs": [experience],

        "Weather_Foggy": [1 if weather == "Foggy" else 0],
        "Weather_Rainy": [1 if weather == "Rainy" else 0],
        "Weather_Snowy": [1 if weather == "Snowy" else 0],
        "Weather_Windy": [1 if weather == "Windy" else 0],

        "Traffic_Level_Low": [1 if traffic == "Low" else 0],
        "Traffic_Level_Medium": [1 if traffic == "Medium" else 0],

        "Time_of_Day_Evening": [1 if time_of_day == "Evening" else 0],
        "Time_of_Day_Morning": [1 if time_of_day == "Morning" else 0],
        "Time_of_Day_Night": [1 if time_of_day == "Night" else 0],

        "Vehicle_Type_Car": [1 if vehicle == "Car" else 0],
        "Vehicle_Type_Scooter": [1 if vehicle == "Scooter" else 0]
    })

    prediction = model.predict(input_df)

    st.success(
        f"Estimated Delivery Time: {prediction[0]:.2f} minutes"
    )