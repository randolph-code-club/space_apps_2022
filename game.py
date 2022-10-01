import time
import random
from functions import typing
from functions import clear
import level1

def game(stats):
    clear()
    typing("Please choose a level by typing the number to begin:")
    print("1) A Beginning")
    # print("2) A Martian Excursion")
    # print("3) Heading for Home")
    level_choice = ""
    while level_choice not in ["1", "2", "3"]:
        level_choice = input("> ")
    if level_choice == "1":
        level1.first_level(stats)
    # if level_choice == "2":
    #     level2.second_level()
    # if level_choice == "3":
    #     level3.third_level()

if __name__ == "__main__":
    game()