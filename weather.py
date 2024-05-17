from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Investigador del clima</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }

            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            h1 {
                text-align: center;
                margin-bottom: 20px;
            }

            label {
                font-weight: bold;
            }

            input[type="text"] {
                width: calc(100% - 70px);
                padding: 8px;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }

            button {
                padding: 8px 20px;
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }

            button:hover {
                background-color: #0056b3;
            }

            #weather-info {
                margin-top: 20px;
            }

            p {
                margin: 5px 0;
            }

            button2 {
                padding: 8px 20px;
                background-color: #ff001e;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }

            .paragraph {
                font-size: 25px;
                line-height: 30;
                font-family: Arial, sans-serif;
            }

            /* Styling for the video element */
            #rain-video {
                width: 320px; /* Adjust the width as needed */
                height: auto; /* Maintain aspect ratio */
                display: none;
                margin: 20px auto; /* Center the video element */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Investigador del clima</h1>
            <form action="/search" method="post">
                <label for="city">Pon una ciudad:</label>
                <input type="text" id="city" name="city">
                <button type="submit">Buscar</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/search', methods=['POST'])
def search_weather():
    city = request.form['city']
    api_key = 'dc228047b3b16e49df8405cfa85cb7b4'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(api_url)
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather = weather_data['weather'][0]['main']

        # Recommendation based on temperature
        recommendation = ""
        if temperature > 28:
            recommendation = "Hace calor alla afuera te recomiendo ponerte unos shorts y una camisa de manga corta, Hidratate plis :)"
        if temperature < 24:
            recommendation = "Hace bastante frio ponte un pantalon y una camisa manga larga. Hacer ejercicios seria muy bueno"
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Weather Investigator</title>
            <style>
                /* CSS styles omitted for brevity */
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Weather Investigator</h1>
                <div id="weather-info">
                    <p class="paragraph">Temperatura: {temperature}°C</p>
                    <p>Humedad: {humidity}%</p>
                    <p>Weather: {weather}</p>
                    <p>{recommendation}</p>
                    <form action="https://awadecoco12.pythonanywhere.com">
                    <button type="submit"> atras </button>
                    </form>
                </div>
            </div>
        </body>
        </html>
        """
    else:
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Error</title>
            <style>
                /* CSS styles omitted for brevity */
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Error</h1>
                <p>Failed to fetch weather data. Please try again later.</p>
            </div>
        </body>
        </html>
        """

if __name__ == '__main__':
    app.run(debug=True)
