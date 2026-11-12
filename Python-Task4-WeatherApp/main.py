
import json
import urllib.request
import urllib.parse
import urllib.error

def get_weather(city):

    # Find the city coordinates
    geo_url = "https://geocoding-api.open-meteo.com/v1/search?"
    params = urllib.parse.urlencode({
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    })

    try:
        request = urllib.request.Request(
            geo_url + params,
            headers={"User-Agent": "PythonWeatherApp"}
        )

        with urllib.request.urlopen(request, timeout=15) as response:
            geo_data = json.loads(response.read().decode())

        if not geo_data.get("results"):
            print("City not found! Please enter a valid city name.")
            return

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        # Get current weather information
        weather_url = "https://api.open-meteo.com/v1/forecast?"

        weather_params = urllib.parse.urlencode({
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
            "timezone": "auto"
        })

        request = urllib.request.Request(
            weather_url + weather_params,
            headers={"User-Agent": "PythonWeatherApp"}
        )

        with urllib.request.urlopen(request, timeout=15) as response:
            weather_data = json.loads(response.read().decode())

        current = weather_data["current"]

        # Weather condition descriptions
        weather_codes = {
            0: "Clear Sky",
            1: "Mainly Clear",
            2: "Partly Cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Depositing Rime Fog",
            51: "Light Drizzle",
            53: "Moderate Drizzle",
            55: "Dense Drizzle",
            61: "Slight Rain",
            63: "Moderate Rain",
            65: "Heavy Rain",
            71: "Slight Snow",
            73: "Moderate Snow",
            75: "Heavy Snow",
            80: "Rain Showers",
            81: "Moderate Rain Showers",
            82: "Heavy Rain Showers",
            95: "Thunderstorm"
        }

        condition = weather_codes.get(
            current["weather_code"], "Unknown Weather Condition"
        )

        print("\n========== WEATHER REPORT ==========")
        print("City:", location["name"])
        print("Country:", location.get("country", "N/A"))
        print("Temperature:", current["temperature_2m"], "°C")
        print("Feels Like:", current["apparent_temperature"], "°C")
        print("Weather:", condition)
        print("Humidity:", current["relative_humidity_2m"], "%")
        print("Wind Speed:", current["wind_speed_10m"], "km/h")
        print("Precipitation:", current["precipitation"], "mm")
        print("====================================")

    except urllib.error.HTTPError as error:
        print("Weather service error:", error.code)

    except urllib.error.URLError:
        print("Network error! Please check your internet connection.")

    except (ValueError, KeyError, TypeError):
        print("Unable to retrieve weather information. Please try again.")


print("====================================")
print("          WEATHER APP")
print("====================================")

city = input("Enter city name: ").strip()

if city:
    get_weather(city)
else:
    print("Please enter a city name.")

print("\nThank you for using Weather App!")
