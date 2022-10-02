from tracemalloc import start
from functions import clear
from functions import typing
import time
from game import game
import inquirer

def startup():
    #Introduction
    clear()
    typing("Welcome to BIOLOGICAL HERO!")
    name_choosing = "n"
    while name_choosing == "n":
        typing("What would you like to name your character?")
        name = input("> ")
        name_conformation = inquirer.prompt([inquirer.Confirm("confirm", message="Would you like to name your character: %s?" % name, default=True)])
        if name_conformation["confirm"]:
            name_choosing = "y"
        else:
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
    explanation = """Your hero, %s, will have 5 stats. Each can be anywhere from 0-10, with 0 being the least powerful and 10 being the most. The stats are:
    - resistance to radiation
    - ability to be alone and stay mentally healthy
    - ability to survive with little nourishment
    - ability to retain bodily health in low/no gravity environments
    - ease of happiness in otherwise harsh environments
    """ % name
    typing(explanation)
    while creating:
        typing("You have %s point(s) left to spend.\n" % points)
        #this line
        questions = [
            inquirer.List("stat", 
            message = "What stat would you like to alter? The stats are", 
            choices = [
            f"radiation ({radiation_resistance}/10)",
            f"isolation ({isolation_resistance}/10)",
            f"starvation ({starvation_resistance}/10)",
            f"gravity ({body_retention}/10)",
            f"enrichment ({ease_of_enrichment}/10)",
            "HELP",
            "RESET"
            ])
        ]
        answer = inquirer.prompt(questions)["stat"]
        if answer == "HELP":
            typing(explanation)
        elif answer == "RESET":
            typing("Ok, resetting.")
            points = 25
            radiation_resistance = 0
            isolation_resistance = 0
            starvation_resistance = 0
            body_retention = 0
            ease_of_enrichment = 0
        else:
            while True:
                try:
                    typing("How many points would you like to modify this stat by?")
                    modification = int(input("> "))
                    if modification <= points:
                        if answer.startswith("radiation") and 10 >= radiation_resistance + modification >= 0:
                            break
                        elif answer.startswith("isolation") and 10 >= isolation_resistance + modification >= 0:
                            break
                        elif answer.startswith("starvation") and 10 >= starvation_resistance + modification >= 0:
                            break
                        elif answer.startswith("gravity") and 10 >= body_retention + modification >= 0:
                            break
                        elif answer.startswith("enrichment") and 10 >= ease_of_enrichment + modification >= 0:
                            break
                    elif modification > points:
                        typing("You don't have enough points left.")
                    elif modification > 10:
                        typing("Each score can be 10 at most.")
                except ValueError:
                    typing("Must be an integer.")
            if answer.startswith("radiation"):
                radiation_resistance += modification
            elif answer.startswith("isolation"):
                isolation_resistance += modification
            elif answer.startswith("starvation"):
                starvation_resistance += modification
            elif answer.startswith("gravity"):
                body_retention += modification
            elif answer.startswith("enrichment"):
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
                        creating = False
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
                
    return {"radiation":radiation_resistance, "isolation":isolation_resistance, "starvation":starvation_resistance, "gravity":body_retention, "enrichment":ease_of_enrichment}
if __name__ == "__main__":
    startup()