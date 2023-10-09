import requests

API_KEY = {"API_KEY"}

city = input("Hava durumunu öğrenmek istediğiniz şehri girin: ")
country = input("Ülkenin kodunu girin (Örneğin TR, US, DE): ")


# for our API Http Requests
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}'

# data request from API
response = requests.get(url)

if response.status_code == 200:
    # take the JSON data arrived from API
    currentWeather = response.json()
    
    # now we can get the info we want
    city_name = currentWeather['name']
    temperature_kelvin = currentWeather['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15
    feels_like = currentWeather['main']['feels_like']
    humidity = currentWeather['main']['humidity']
    wind_speed = currentWeather['wind']['speed']
    
    # PRINT RESULTS
    
    print(f"\n{city_name} şehrindeki anlık hava durumu:")
    print(f"Sıcaklık: {temperature_celsius:.2f} C")
    print(f"Nem Oranı: %{humidity}")
    print(f"Rüzgar hızı: {wind_speed} m/s")
    
else:
    print("Hava durumu verileri alınamadı. Lütfen şehir ve ülke kodunuzu kontrol ediniz.")
