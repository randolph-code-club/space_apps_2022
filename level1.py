import time
import random
from functions import typing, clear, radiation_scenario, isolation_scenario1, isolation_scenario2, win
from functions import starvation_scenario1, starvation_scenario2, enrichment_scenario1, enrichment_scenario2



def first_level(stats):
    possible_levels = [radiation_scenario, isolation_scenario1, isolation_scenario2, \
    starvation_scenario1, starvation_scenario2, enrichment_scenario1, enrichment_scenario2]
    levels = []
    for i in range(3):
        levels.append(possible_levels.pop(possible_levels.index(random.choice(possible_levels))))

    clear()
    typing("You have chosen level 1. Prepare to begin your journey.")
    time.sleep(2)
    clear()
    typing("On the previous mission to Mars, Journier 4, one astronaut dropped his wallet on the Martian surface, and left it behind.")
    typing("You receive a call from the space organization asking you to go on an expedition to Mars to retrieve the wallet.")
    typing("You are told that because of your biological advantages, you will be the only person on the mission. Nobody else is going due to budget cuts.")
    typing("A few weeks later, you board the rocket to embark on the mission Journier 4 1/2.")
    time.sleep(2)
    clear()
    typing("3")
    time.sleep(1)
    typing("2")
    time.sleep(1)
    typing("1")
    time.sleep(1)
    typing("Ignition!")
    time.sleep(1)
    typing("Your rocket lifts from the ground, and a few minutes later, you are in orbit around Earth.")
    typing("Fast forward a little while, you are on your way to Mars.")
    time.sleep(2)
    for level in levels:
        level(stats)
        print("Press enter to continue.")
        input("> ")
    win()

if __name__ == "__main__":
    first_level()