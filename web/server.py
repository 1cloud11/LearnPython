from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city("Kiev,Ukraine")
    if weather:
        return f"В киеве сейчас {weather['temp_C']}. Ощущается как {weather['FeelsLikeC']}"
    else:
        return "Сервис погоды временно недоступен"
if __name__ == "__main__":
    app.run(debug=True)