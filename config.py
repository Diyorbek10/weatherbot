import requests

API_TOKEN = '2014303894:AAFPdvMywH7X3-VSzmrwX7hVGnOXgU-zJtA'
API_weather = '11383a422946d6690d8e97982829c739'
api_url = 'https://api.openweathermap.org/data/2.5/weather'


def getWeather(city):
    r = requests.post(url=api_url, params={'q': city, 'APPID': API_weather, 'units': 'metric'})
    return r