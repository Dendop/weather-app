from flask import Flask, render_template, request, jsonify
import configparser
import requests


API_KEY = os.environ.get('api_key')
BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__)

def get_icon_filename(weather_id):
    if 200 <= weather_id < 300:
        return 'thunder.svg'
    elif 300 <= weather_id < 500:
        return 'drizzle.svg'
    elif 500 <= weather_id < 502:
        return 'light_rain.svg'
    elif 502 <= weather_id < 600:
        return 'heavy_rain.svg'
    elif 600 <= weather_id < 700:
        return 'snow.svg'
    elif 700 <= weather_id < 800:
        return 'mist.svg'
    elif weather_id == 800:
        return 'clear_sky.svg'
    elif weather_id > 800:
        return 'clouds.svg'
    else:
        return f"something went wrong"

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        
        data = request.get_json()
        city_name = data.get("city")#this gets the city from front end
        units = data.get("units")#this gets the required units
        
        url = (
            f"{BASE_WEATHER_API_URL}?q={city_name}" 
            f"&units={units}&appid={API_KEY}"
        )
        try:
            
            response = requests.get(url)
            
            
            data = response.json()
            
            
            #if success
            if response.status_code == 200:
                 
                description = data['weather'][0]['description']
                temperature = data['main']['temp']
                weather_id = data['weather'][0]['id'] #for more advanced "icon"
                print("weather ID : ", weather_id)
                
                icon_filename = get_icon_filename(weather_id)
                
                return  jsonify({
                    "city_name": city_name,
                    "temperature": f"{temperature}°",
                    "description": description,
                    "icon_filename" : icon_filename
                })
                
            else:
                error_message = data.get("message", "Unable to fetch weather data") 
                print("Error message:", error_message)   
                return render_template("layout.html", error_message=error_message)
        
        except Exception as e:
            print("Exception occured", e)
            return render_template("layout.html")
    
    print()
    return render_template("layout.html")


