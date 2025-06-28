import requests

API_KEY = "7339281eef78247a5ec9dbe1e3a2d00d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name (like Chennai,IN): ")
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    weather = data['weather'][0]['description']
    print(f"\n Temperature in {city}: {temperature}°C")
    print(f" Weather: {weather}")

else:
    print("\n❌ Error fetching weather data. Please check city name or try again later.")
