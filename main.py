import streamlit as st
import pandas as pd

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place:")
days = st.slider(label="Forecast Days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days.")
option = st.selectbox(label="Select Data to view:",
                    options=("Temperature", "Cloud"))

st.subheader(f"{option} for the next {days} days in {place}")