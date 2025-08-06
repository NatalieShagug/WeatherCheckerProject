# Weather Checker App


###  App Overview
This simple weather checker app lets users enter the name of any city and instantly see real-time weather information. It displays the current temperature, feels-like temperature, a short weather description, and humidity level.

### How to Run the Project Locally
1. Clone this repository from GitHub:
```bash
git clone https://github.com/NatalieShagug/WeatherCheckerProject.git
```

2. Install dependencies:

If you're using Poetry:

```bash
poetry install
```

Or if you're using pip:

```bash
pip install -r requirements.txt
```

---

3.Run the Streamlit app:

```bash
poetry run .streamlit run app.py
```

A browser window will open with the app:  
Enter a city name and get real-time weather information.

---
**Note**:

The file main.py contains the function that connects to the weather API. You don't run this file directly. It's used by app.py behind the scenes when you launch the app.

**Important**:

To use the app with your own OpenWeatherMap API key, update the API_KEY variable inside the secrets.toml file with your personal key.You can get a free key by signing up at openweathermap.org.

### Try the App online:  
[Weather Checker on Streamlit Cloud](https://weathercheckerproject-6nb23f4mseuepcq8jqumn3.streamlit.app/)
