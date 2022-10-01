import time
import random
from functions import typing, clear
import level1

def game():
    clear()
    typing("Please choose a level by typing the number to begin:")
    print("1) A Beginning")
    level_choice = ""
    while level_choice not in ["1"]:
        level_choice = input("> ")
    if level_choice == "1":
        level1.first_level()
    # if level_choice == "2":
    #     level2.second_level()
    # if level_choice == "3":
    #     level3.third_level()

if __name__ == "__main__":
    game()