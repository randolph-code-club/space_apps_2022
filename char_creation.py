from tracemalloc import start
from functions import clear
from functions import typing
def startup():
    #Introduction
    clear()
    typing("Welcome to INSERT GAME TITLE HERE!\n")
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
    explanation = """
    Your hero will have 5 stats. Each can be anywhere from 0-10, with 0 being the least powerful and 10 being the most. The stats are:
    - resistance to radiation
    - ability to be alone and stay mentally healthy
    - ability to survive with little nourishment
    - ability to retain bodily health in low/no gravity environments
    - ease of happiness in otherwise harsh environments
    """
    typing(explanation)
    while creating:

        typing("You have %s points left to spend.\n" % points)
        typing("What stat would you like to alter? The stats are:\n- 'radiation'\n- 'isolation'\n- 'starvation'\n- 'gravity'\n- 'enrichment'\nType 'help' to see the explanation again.")
        answer = input("> ").lower()
        if answer in ("radiation", "isolation", "starvation", "gravity", "enrichment"):
            while True:
                try:
                    typing("How many points would you like to modify this stat by?")
                    modification = int(input("> "))
                    if modification <= points:
                        break
                    elif modification > points:
                        typing("You don't have that many points left.")
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
        elif answer == "help":
            typing(explanation)
        else:
            print("I didn't get that, please try again.")

if __name__ == "__main__":
    startup()