import os
import requests
from image import DrawImage
import random
from functions import clear
from functions import typing
import time

def second_level(stats):

    from dotenv import load_dotenv

    load_dotenv()

    clear()

    image_url = None
    earth_date = None

    api_key = os.environ["NASA_API_KEY"]

    while not image_url:
        sol = random.randint(1, 3423)
        image_response = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={api_key}")
        image_data = image_response.json()
        if len(image_data["photos"]) > 0:
            image_url = image_data["photos"][0]["img_src"]
            earth_date = image_data["photos"][0]["earth_date"]
            rover_name = image_data["photos"][0]["rover"]["name"]

    # image = DrawImage.from_url(image_url, (100, 30))
    # image.draw_image()

    weather_response = requests.get(f"https://api.maas2.apollorion.com/{sol}")
    weather_data = weather_response.json()
    

    typing("You have selected level 2. Prepare to begin your Martian expedition.")
    time.sleep(2)
    clear()
    typing("After ages of travelling, you finally arrive at Mars.")
    typing("You engage your lander and descend to the surface.")
    typing(f"You have just landed on Mars. It is currently {earth_date} on Earth.")
    time.sleep(2)
    clear()
    typing("You have made it far already, but now it is time to achieve the aim of your mission:")
    time.sleep(1)
    typing("You must locate the wallet.")
    time.sleep(1)
    typing("You check the temperature, air pressure, and UV radiation index.")
    print(f"Downloading Data and Imagery from {rover_name} Rover", end = "")
    time.sleep(1)
    print(".", end = "")
    for i in range(2):
        time.sleep(1)
        print(".", end = "")
    print()

    image = DrawImage.from_url(image_url, (100, 30))
    image.draw_image()

    typing("Pressure: {} mb".format(weather_data["pressure"]))
    typing("UV Index: {}".format(weather_data["local_uv_irradiance_index"]))
    typing("Max Temp: {}°C".format(weather_data["max_temp"]))
    typing("Min Temp: {}°C".format(weather_data["min_temp"]))
    time.sleep(2)
    typing("Press Enter to continue")
    input("> ")
    clear()

    typing("After a long time in zero gravity, your body has suffered detremental effects.")
    if stats["gravity"] == 0:
        pass #WizardGrayFire start here

if __name__ == "__main__":
    second_level()