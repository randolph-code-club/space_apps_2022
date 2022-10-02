import random
from functions import clear, typing, lose, win
from functions import radiation_scenario, isolation_scenario1, isolation_scenario2, enrichment_scenario1, enrichment_scenario2
from functions import starvation_scenario1, starvation_scenario2
import time

def third_level(stats, remaining_scenarios):
    scenarios = [random.choice(remaining_scenarios) for i in range(3)]

    typing("You have chosen level 3, the third and final level of the game.")
    time.sleep(2)
    clear()
    typing("It's time to go home, but remember that you still have challenges ahead of you.")
    time.sleep(1)
    for level in scenarios:
        level(stats)
        print("Press enter to continue.")
        input("> ")
    clear()
    typing("After a while, you can see Earth from the window of your spaceship. You prepare for rentry.")
    time.sleep(1)
    typing("You splash down into the Pacific Ocean.")
    typing("You have made it home with your wallet.")
    typing("Although I think you may have left your keys behind on this trip...")
    win()

if __name__ == "__main__":
    third_level()