import requests
from flask import current_app
from config import Config

def get_weather(city):
    """Fetch current weather and return clean JSON"""
    api_key = Config.OWM_API_KEY
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # If something goes wrong, return the error
    if data.get("cod") != 200:
        return {"error": data.get("message", "Unable to fetch weather")}

    # Extract clean info
    result = {
        "city": data.get("name"),
        "country": data["sys"].get("country"),
        "temperature": f"{data['main']['temp']}°C",
        "feels_like": f"{data['main']['feels_like']}°C",
        "description": data["weather"][0].get("description").capitalize(),
        "humidity": f"{data['main']['humidity']}%",
        "pressure": f"{data['main']['pressure']} hPa",
        "wind_speed": f"{data['wind']['speed']} m/s"
    }

    return result


def get_forecast(city):
    """Fetch 5-day forecast"""
    api_key = Config.OWM_API_KEY
    base_url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("cod") != "200":
        return {"error": data.get("message", "Unable to fetch forecast")}

    # Extract 5 forecast entries (every 3 hours)
    forecasts = []
    for entry in data["list"][:5]:
        forecasts.append({
            "datetime": entry["dt_txt"],
            "temp": f"{entry['main']['temp']}°C",
            "description": entry["weather"][0]["description"].capitalize()
        })

    return {
        "city": data["city"]["name"],
        "country": data["city"]["country"],
        "forecast": forecasts
    }
