import streamlit as st
from src.predict import predict_house


# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)


# Title
st.title("🏠 House Price Predictor")

st.write(
    "Enter the details of a house below to estimate its price "
    "using a Linear Regression model."
)


st.divider()


# House information
st.subheader("House Information")


col1, col2 = st.columns(2)


with col1:

    med_inc = st.number_input(
        "Median Income",
        min_value=0.0,
        value=5.0,
        step=0.1
    )

    house_age = st.number_input(
        "House Age",
        min_value=0.0,
        value=20.0,
        step=1.0
    )

    ave_rooms = st.number_input(
        "Average Rooms",
        min_value=0.0,
        value=6.0,
        step=0.1
    )

    ave_bedrms = st.number_input(
        "Average Bedrooms",
        min_value=0.0,
        value=1.0,
        step=0.1
    )


with col2:

    population = st.number_input(
        "Population",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

    ave_occup = st.number_input(
        "Average Occupancy",
        min_value=0.0,
        value=3.0,
        step=0.1
    )

    latitude = st.number_input(
        "Latitude",
        value=34.0,
        step=0.1
    )

    longitude = st.number_input(
        "Longitude",
        value=-118.0,
        step=0.1
    )


st.divider()


# Prediction button
if st.button("Predict House Price", type="primary"):

    features = [
        med_inc,
        house_age,
        ave_rooms,
        ave_bedrms,
        population,
        ave_occup,
        latitude,
        longitude
    ]

    price = predict_house(features)

    st.success("Prediction completed!")

    st.metric(
        label="Estimated House Price",
        value=f"${price:,.2f}"
    )