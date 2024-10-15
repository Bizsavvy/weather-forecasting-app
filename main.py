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

d, t = get_data(place, days, option)

figure = px.line(x=d, y=t,
                 labels={"x": "Date", "y": "Temperature(C)"})
st.plotly_chart(figure)
