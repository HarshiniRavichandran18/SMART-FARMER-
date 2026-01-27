from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔑 Put your OpenWeatherMap API key here
API_KEY = "2266c4f5af23f1a9f1de0b49f3981a7e"

@app.route("/", methods=["GET", "POST"])
def home():
    city = "Chennai"  # default city
    if request.method == "POST":
        city_input = request.form.get("city")
        if city_input:
            city = city_input

    # OpenWeatherMap API call
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Handle invalid city
    if data.get("cod") != 200:
        weather = {
            "city": city,
            "temp": "N/A",
            "description": "City not found",
            "humidity": "N/A"
        }
    else:
        weather = {
            "city": city,
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
