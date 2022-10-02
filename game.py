import time
import random
from functions import typing, level1_got_completed, level2_got_completed
from functions import clear, is_level1_completed, is_level2_completed
import level1
import level2
import level3

def game(stats):
    clear()
    typing("Please choose a level by typing the number to begin:")
    print("1) A Beginning")
    print("2) A Martian Excursion" if is_level1_completed() else "") 
    print("3) Heading for Home" if is_level1_completed() and is_level2_completed() else "")
    level_choice = ""
    while level_choice not in ["1", "2", "3"]:
        level_choice = input("> ")
    if level_choice == "1":
        remaining_scenarios = level1.first_level(stats)
        level1_got_completed()
    if level_choice == "2" and is_level1_completed():
        level2.second_level(stats)
        level2_got_completed()
    if level_choice == "3" and is_level1_completed() and is_level2_completed():
        level3.third_level(stats, remaining_scenarios)

if __name__ == "__main__":
    game()