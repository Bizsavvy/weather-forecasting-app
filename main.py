import streamlit as st
import plotly.express as px
import pandas as pd
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place:")
days = st.slider(label="Forecast Days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days.")
option = st.selectbox(label="Select Data to view:",
                      options=("Temperature", "Cloud"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the temperature/cloud data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Cloud":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            print(sky_conditions)
            images = {"Rain": "images/rain.png", "Clouds": "images/cloud.png",
                      "Clear": "images/clear.png", "Snow": "images/snow.png"}
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=115)
    except KeyError:
        st.error("Please Enter a Valid City name.")