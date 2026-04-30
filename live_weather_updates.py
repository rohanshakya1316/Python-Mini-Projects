from dotenv import load_dotenv
import requests
import os 

load_dotenv()
# 🔑 Put your API key here
API_KEY = os.getenv("WEATHER_API_KEY")
print(API_KEY)

def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        print(url)
        response = requests.get(url)
        data = response.json()

        # ❌ Handle invalid city or API error
        if response.status_code != 200:
            print("\n❌ Error:", data.get("message", "Something went wrong"))
            return

        # ✅ Extract useful data
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        # 🌤️ Output
        print("\n🌍 Location:", f"{city_name}, {country}")
        print("🌡️ Temperature:", f"{temp}°C")
        print("🤔 Feels Like:", f"{feels_like}°C")
        print("💧 Humidity:", f"{humidity}%")
        print("🌥️ Condition:", weather_desc.title())
        print("🌬️ Wind Speed:", f"{wind_speed} m/s")

    except requests.exceptions.RequestException:
        print("\n❌ Network error. Check your internet connection.")

def main():
    print("====== 🌦️ Live Weather App ======")
    
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        
        if city.lower() == "exit":
            print("👋 Exiting program...")
            break
        
        print("🔎 Fetching weather...")
        get_weather(city)

if __name__ == "__main__":
    main()