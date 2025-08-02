import streamlit as st
from main import get_weather_data

st.title("Weather Checker App")
st.markdown("Check the current weather in any city")
city_name = st.text_input("Enter City Name : ")
if st.button("Check Weather"):
    if city_name:
        weather_data = get_weather_data(city_name)
        st.code(weather_data)
    else:
        st.warning("Please check the city name.")