from flask import Blueprint, request, jsonify, current_app
from services import openweather

bp = Blueprint('weather', __name__, url_prefix="/api")

@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@bp.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    units = request.args.get("units", "metric")

    cache_key = f"weather:{city or lat+','+lon}:{units}"
    cached = current_app.cache.get(cache_key)
    if cached:
        return jsonify(cached)

    try:
        if city:
            result = openweather.current_weather_by_city(city)
        elif lat and lon:
            result = openweather.current_weather_by_coords(lat, lon)
        else:
            return jsonify({"error": "Provide ?city=NAME or ?lat=..&lon=.."}), 400

        out = {
            "location": result.get("name"),
            "coords": result.get("coord"),
            "weather": result.get("weather"),
            "temp": result.get("main"),
            "wind": result.get("wind"),
        }
        current_app.cache.set(cache_key, out, timeout=current_app.config.get("CACHE_TIMEOUT", 600))
        return jsonify(out)
    except Exception as e:
        return jsonify({"error": "Unable to fetch weather", "details": str(e)}), 502

@bp.route("/forecast", methods=["GET"])
def forecast():
    city = request.args.get("city")
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    units = request.args.get("units", "metric")

    cache_key = f"forecast:{city or lat+','+lon}:{units}"
    cached = current_app.cache.get(cache_key)
    if cached:
        return jsonify(cached)

    try:
        if city:
            result = openweather.forecast_by_city(city)
        elif lat and lon:
            result = openweather.forecast_by_coords(lat, lon)
        else:
            return jsonify({"error": "Provide ?city=NAME or ?lat=..&lon=.."}), 400

        simplified = [
            {"dt_txt": item.get("dt_txt"), "main": item.get("main"), "weather": item.get("weather")}
            for item in result.get("list", [])
        ]
        out = {"city": result.get("city"), "count": len(simplified), "forecasts": simplified}
        current_app.cache.set(cache_key, out, timeout=current_app.config.get("CACHE_TIMEOUT", 600))
        return jsonify(out)
    except Exception as e:
        return jsonify({"error": "Unable to fetch forecast", "details": str(e)}), 502
