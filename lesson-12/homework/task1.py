import requests

def get_weather(api_key, city="Tashkent"):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use Celsius (change to "imperial" for Fahrenheit)
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTP errors
        
        data = response.json()
        
        # Extract relevant data
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]
        
        # Print formatted output
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather_desc.capitalize()}")
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Error: Invalid API key.")
        elif response.status_code == 404:
            print("Error: City not found.")
        else:
            print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"
get_weather(API_KEY, "Tashkent")  # Replace "Tashkent" with any city
