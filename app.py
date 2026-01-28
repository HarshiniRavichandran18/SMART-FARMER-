from flask import Flask
from routes.weather_routes import weather_bp

app = Flask(__name__)
app.register_blueprint(weather_bp)

# Render uses this
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
