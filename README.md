## Introduction:
This is a simple weather web app that will show you the temperature based on the user's city input. It's hosted on Render, using the api key from [OpenWeather](https://openweathermap.org/city/2643743). <br>I have built also similar [weather_cli_app](https://github.com/Dendop/Leetcode-practice/tree/main/weather_cli_app) that runs on local machine using the terminal.
<br>

## Usage:
The app takes the input from the user, the name of the city. After entering the city, you will be shown the temperature, description and icon.

## How it works:
[main.js](https://github.com/Dendop/weather-app/blob/main/main/static/js/main.js) stores the city name and units and sends the POST to the [Flask backend](https://github.com/Dendop/weather-app/blob/main/main/__init__.py). The Flask sends requests with stored 'secret' api key together with the 'city name' and receives JSON data. The Flask handles the data and icon image based on weather_id then returns them back to [main.js](https://github.com/Dendop/weather-app/blob/main/main/static/js/main.js). If the data exists, then they are sent back to [layout.html](https://github.com/Dendop/weather-app/blob/main/main/templates/layout.html)

## Requirements:
Can be found [here](https://github.com/Dendop/weather-app/blob/main/requirements.txt) 'gunicorn' is used for Render.
To install requirements type in your terminal `pip install -r requirements.txt`

### Additional:
You will need to register with [OpenWeather](https://openweathermap.org/city/2643743) to get api key, either store it in local machine with separate file or if you want to deploy it on [Render](https://render.com/)


