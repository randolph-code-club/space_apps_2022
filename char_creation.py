from tracemalloc import start
from functions import clear
from functions import typing
import time

def startup():
    #Introduction
    clear()
    typing("Welcome to BIOLOGICAL HERO!\n")
    name_choosing = "n"
    while name_choosing == "n":
        typing("What would you like to name your character?\n")
        name = input("> ")
        clear()
        typing("Would you like to name your character: %s? (y/n)\n" % name)
        name_conformation = ""
        while name_conformation not in ["y", "n"]:
            name_conformation = input("> ")
        if name_conformation == "y":
            name_choosing = "y"
        elif name_conformation == "n":
            pass
    clear()
    typing("You have named your superhero %s.\n" % name)

    #Stats declaration
    points = 25 #total points that can be spent
    radiation_resistance = 0 #how well they withstand radiation
    isolation_resistance = 0 #sanity retention without human contact
    starvation_resistance = 0 #needs less food/water
    body_retention = 0 #how well they withstand lack of gravity
    ease_of_enrichment = 0 #how little the hero needs to be happy
    
    creating = True
    #explanation subject to change
    explanation = """Your hero will have 5 stats. Each can be anywhere from 0-10, with 0 being the least powerful and 10 being the most. The stats are:
    - resistance to radiation
    - ability to be alone and stay mentally healthy
    - ability to survive with little nourishment
    - ability to retain bodily health in low/no gravity environments
    - ease of happiness in otherwise harsh environments
    """
    typing(explanation)
    while creating:
        typing("You have %s points left to spend.\n" % points)
        typing("What stat would you like to alter? The stats are:")
        print("- 'radiation'\n- 'isolation'\n- 'starvation'\n- 'gravity'\n- 'enrichment'")
        typing("Type \"help\" to see the explanation again or \"reset\" to reset your stats.")
        answer = input("> ").lower()
        if answer in ("radiation", "isolation", "starvation", "gravity", "enrichment"):
            while True:
                try:
                    typing("How many points would you like to modify this stat by?")
                    modification = int(input("> "))
                    if modification <= points:
                        if answer == "radiation" and 10 >= radiation_resistance + modification >= 0:
                            break
                        elif answer == "isolation" and 10 >= isolation_resistance + modification >= 0:
                            break
                        elif answer == "starvation" and 10 >= starvation_resistance + modification >= 0:
                            break
                        elif answer == "gravity" and 10 >= body_retention + modification >= 0:
                            break
                        elif answer == "enrichment" and 10 >= ease_of_enrichment + modification >= 0:
                            break
                    elif modification > points:
                        typing("You don't have enough points left.")
                    elif modification > 10:
                        typing("Each score can be 10 at most.")
                except ValueError:
                    typing("Must be an integer.")

            if answer == "radiation":
                radiation_resistance += modification
            elif answer == "isolation":
                isolation_resistance += modification
            elif answer == "starvation":
                starvation_resistance += modification
            elif answer == "gravity":
                body_retention += modification
            elif answer == "enrichment":
                ease_of_enrichment += modification
            points -= modification

            if points == 0:
                typing(f"""Your hero's stats are:
- radiation resistance: {radiation_resistance}
- ability to stay mentally healthy when lonely: {isolation_resistance}
- ability to live off of few resources: {starvation_resistance}
- ability to retain bodily health in low/no gravity: {body_retention}
- ease of enrichment in otherwise harsh environments: {ease_of_enrichment}
                """)
                typing("Are these the stats you want? Please answer 'y' or 'n'.")
                while True:
                    yesNo = input("> ").lower().strip()
                    if yesNo == "y":
                        creating = False
                        typing("Your stats have been set.")
                        time.sleep(2)
                        break
                    elif yesNo == "n":
                        typing("Ok, resetting.")
                        points = 25
                        radiation_resistance = 0
                        isolation_resistance = 0
                        starvation_resistance = 0
                        body_retention = 0
                        ease_of_enrichment = 0
                        break
                    else:
                        typing("Please try again.")
                
        elif answer == "help":
            typing(explanation)
        elif answer == "stats":
            typing(f"""Your hero's current stats are:
- radiation resistance: {radiation_resistance}/10
- ability to stay mentally healthy when lonely: {isolation_resistance}/10
- ability to live off of few resources: {starvation_resistance}/10
- ability to retain bodily health in low/no gravity: {body_retention}/10
- ease of enrichment in otherwise harsh environments: {ease_of_enrichment}/10
            """)
        elif answer == "reset":
            typing("Ok, resetting.")
            points = 25
            radiation_resistance = 0
            isolation_resistance = 0
            starvation_resistance = 0
            body_retention = 0
            ease_of_enrichment = 0
        else:
            typing("I didn't get that, please try again.")

if __name__ == "__main__":
    startup()