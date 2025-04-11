from flask import Flask, render_template, request, jsonify
import configparser
import requests

config = configparser.ConfigParser()
config.read('secrets.ini')
API_KEY = config['openweather']['api_key']
BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__)

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
            #print(response.status_code)
            
            data = response.json()
            #print("Response JSON:", data)
            
            #if success
            if response.status_code == 200:
                
                description = data['weather'][0]['description']
                temperature = data['main']['temp']
                weather_id = data['weather'][0]['id'] #for more advanced
                #print("Description", description)
                #print("temperature", temperature)
                #print(city_name)
                
                return  jsonify({
                    "city_name": city_name,
                    "temperature": f"{temperature}°",
                    "description": description
                    
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


