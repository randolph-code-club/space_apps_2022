import os
import requests
from image import DrawImage
import random
from functions import clear, typing, lose, win, lost_one, count_lost
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
    time.sleep(1)
    typing("Press Enter to continue")
    input("> ")
    clear()

    typing("After a long time in zero gravity, your body has suffered detremental effects.")
    if stats["gravity"] == 0:
        typing("Due to your body retention score of 0, your muscles have seriously declined in functionality. You fear that you may not be able to lift your wallet.") #~~you didn't understand the gravity of the situation until it was too late~~
        lose()
    elif stats["gravity"] == 10:
        typing("Due to your body retention score of 10, your superpowers have kept your muscles strong and your bones sturdy, dispite the lack of excercise equipment due to budget cuts.")
    elif stats["gravity"] <= 5:
        typing(f"Your body retention score of {stats['gravity']} lets you still move normally after some hassle, but every part of you and every object you encounter seems unreasonably heavy for what it is.")
        lost_one()
    elif stats["gravity"] > 5:
        typing(f"Your body retention score of {stats['gravity']} means you're a bit wobbly at first, but after a time you manage to get reaquainted with gravity and start moving normally again.")
    time.sleep(1)
    typing("Press Enter to continue")
    input("> ")
    if count_lost() >= 4:
        lose()
    typing("You decide to exit your spacecraft and walk on the Martian surface to find your wallet.")
    if weather_data["local_uv_irradiance_index"] == "Low":
        typing("The UV Index is {}, so you will be fine.".format(weather_data["local_uv_irradiance_index"]))
    elif weather_data["local_uv_irradiance_index"] <= "Moderate":
        typing("The UV Index is {}; that's pretty high.".format(weather_data["local_uv_irradiance_index"]))
        if stats["radiation"] == 0:
            typing("Because you have a radiation resistance level of 0, you are unable to cope with it.")
            lose()
    else:
        typing("Due to the UV Index of {}, you may suffer serious detremental effects.".format(weather_data["local_uv_irradiance_index"]))
        if stats["radiation"] == 0:
            typing("Your radiation resistance level of 0 does nothing to stop the full brunt of the radiation, and your suit does nothing against it either due to budget cuts.")
            lose()
        elif stats["radiation"] == 10:
            typing("Your radiation resistance level of 10 causes you to not even be affected by this.")
        elif stats["radiation"] <= 5:
            typing("Your radiation resistance level of %s causes you to feel significanty hotter than usual." % stats["radiation"])
            lost_one()
        elif stats["radiation"] > 5:
            typing("Your radiation resistance level of %s allows you to not be bothered by this, ." % stats["radiation"])
    if count_lost() >= 4:
        lose()
    time.sleep(2)
    clear()
    typing("You walk across the surface for hours, trying to remember where you saw your wallet last.")
    typing("And then... you finally see it.")
    typing("It is partially covered in red dust, but that's okay.")
    time.sleep(1)
    typing("You also see that your credit card has expired.")
    time.sleep(1)
    typing("You pick up the wallet and return to your spacecraft.")
    typing("You hop aboard and take off towards home!")
    win()

if __name__ == "__main__":
    second_level()