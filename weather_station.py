import random

def get_weather_data():
    temperature = random.randint(20, 40)
    humidity = random.randint(40, 90)

    print("\nWeather Station Data")
    print("--------------------")
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")

while True:
    get_weather_data()

    choice = input("\nGenerate new reading? (y/n): ")

    if choice.lower() != 'y':
        break
