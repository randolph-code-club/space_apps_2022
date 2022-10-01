import os
import requests
from image import DrawImage
import functions

functions.clear()

sol = "3423"

api_key = os.environ["NASA_API_KEY"]
image_response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={}&api_key={}".format(sol, api_key))
image_data = image_response.json()
image_url = image_data["photos"][0]["img_src"]

image = DrawImage.from_url(image_url, (100, 30))
image.draw_image()

weather_response = requests.get("https://api.maas2.apollorion.com/{}".format(sol))
weather_data = weather_response.json()
print("Pressure: {}".format(weather_data["pressure"]))
print("UV Index: {}".format(weather_data["local_uv_irradiance_index"]))
print("Max Temp: {}".format(weather_data["max_temp"]))
print("Min Temp: {}".format(weather_data["min_temp"]))
