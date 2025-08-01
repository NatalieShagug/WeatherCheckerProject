import requests

API_KEY = "Your_API_KEY"
url = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city_name) :
    params = {"q": city_name, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    if response.status_code == 200 :
        data = response.json()
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather_description = data["weather"][0]["description"]
        air_humidity = data["main"]["humidity"]

        return f"Location: {city_name}\nTemperature: {temperature}°C\nFeels like: {feels_like}°C\nCondition: {weather_description}\nHumidity: {air_humidity}%"

    else:
        return f"Error: Please check the city name."


