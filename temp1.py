import requests

base_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
api_key = "b6907d289e10d714a6e88b30761fae22"

city = "London,us"

while True:
    print("Choose an option:")
    print("1. Get Temperature")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exiting the program.")
        break
    elif choice == "1":
        response = requests.get(f"{base_url}?q={city}&appid={api_key}")
        data = response.json()
        temperature = data['list'][0]['main']['temp']
        print(f"Temperature: {temperature} K")
    elif choice == "2":
        response = requests.get(f"{base_url}?q={city}&appid={api_key}")
        data = response.json()
        wind_speed = data['list'][0]['wind']['speed']
        print(f"Wind Speed: {wind_speed} m/s")
    elif choice == "3":
        response = requests.get(f"{base_url}?q={city}&appid={api_key}")
        data = response.json()
        pressure = data['list'][0]['main']['pressure']
        print(f"Pressure: {pressure} hPa")
    else:
        print("Invalid choice. Please select a valid option.")