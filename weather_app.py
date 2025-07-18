import requests

# Replace with your real API key
API_KEY = "25d363655238ae73c86879e40b12cf95"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Ask the user to enter a city
city = input("Enter city name: ")

# Create the full API URL
url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"

# Send a GET request to the API
response = requests.get(url)

# Check the response
if response.status_code == 200:
    data = response.json()
    main = data['main']
    wind = data['wind']
    weather = data['weather'][0]

    print(f"\nWeather in {city.title()}:")
    print(f"Temperature: {main['temp']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Wind Speed: {wind['speed']} m/s")
    print(f"Condition: {weather['description'].title()}")
else:
    print("City not found or API error.")
