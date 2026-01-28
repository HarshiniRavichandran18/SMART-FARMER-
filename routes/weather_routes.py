from flask import Blueprint, jsonify, request
from services.weather_service import get_weather

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City is required"}), 400

    data = get_weather(city)
    if not data:
        return jsonify({"error": "Unable to fetch weather data"}), 500

    return jsonify(data)
