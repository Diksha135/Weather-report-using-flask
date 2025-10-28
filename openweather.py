import requests
from config import Config

BASE_URL = "https://api.openweathermap.org/data/2.5"

def _get(path, params):
    if not Config.OWM_API_KEY:
        raise RuntimeError("OWM_API_KEY not set")
    params = params.copy()
    params["appid"] = Config.OWM_API_KEY
    params["units"] = params.get("units", "metric")
    url = f"{BASE_URL}/{path}"
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def current_weather_by_city(city_name):
    return _get("weather", {"q": city_name})

def current_weather_by_coords(lat, lon):
    return _get("weather", {"lat": lat, "lon": lon})

def forecast_by_city(city_name):
    return _get("forecast", {"q": city_name})

def forecast_by_coords(lat, lon):
    return _get("forecast", {"lat": lat, "lon": lon})
