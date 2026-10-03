import requests
api_key="fe9bc9d0bc54f69654c49ae1743e99d3"
print("===welcom to weather app===")
user_input=input(" city:")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
 weather=weather_data.json()['weather'][0]['main']
 temp=weather_data.json()['main']['temp']
 celcius=(temp-32)/1.8
 celcius=float(celcius)
 print(f"The weather in {user_input} is: {weather}")
 print(f"The temperature in {user_input} is: {celcius}ºc")