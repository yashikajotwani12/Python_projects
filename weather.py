import requests
from pprint import pprint

Api_key='8811a8392de52133ae4e09659127b048'

city = input("Enter a city: ")
base_url ="http://api.openweathermap.org/data/2.5/weather?appid="+Api_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
