import requests
import os
def get_weather(city:str):
    key = os.getenv("OPENWEATHER_API_KEY")
    if not key:
        raise ValueError("环境变量 WEATHER_KEY 未设置")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q":city,
        "appid":key, 
        "units": "metric",
        "lang": "zh_cn"  
    }
    resp = requests.get(url,params=params)
    if resp.status_code == 200: 
        data = resp.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
    return f"{city}的天气是{weather}，气温是{temp},气温范围{temp_min}-{temp_max}"

city = input("pleast type city name: ")

response = get_weather(city)

print(response)