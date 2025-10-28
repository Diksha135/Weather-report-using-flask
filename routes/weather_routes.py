from flask import Blueprint, request, jsonify, current_app
from services.weather_service import get_weather, get_forecast

bp = Blueprint("weather", __name__, url_prefix="/api")

@bp.route("/weather", methods=["GET"])
def weather():
    """Get current weather for a given city."""
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    cached_data = current_app.cache.get(city)
    if cached_data:
        return jsonify(cached_data)

    data = get_weather(city)
    if isinstance(data, tuple):  # error case
        return jsonify(data[0]), data[1]

    current_app.cache.set(city, data, timeout=current_app.config["CACHE_TIMEOUT"])
    return jsonify(data)


@bp.route("/forecast", methods=["GET"])
def forecast():
    """Get 5-day weather forecast for a given city."""
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    cache_key = f"{city}_forecast"
    cached_data = current_app.cache.get(cache_key)
    if cached_data:
        return jsonify(cached_data)

    data = get_forecast(city)
    if isinstance(data, tuple):  # error case
        return jsonify(data[0]), data[1]

    current_app.cache.set(cache_key, data, timeout=current_app.config["CACHE_TIMEOUT"])
    return jsonify(data)
