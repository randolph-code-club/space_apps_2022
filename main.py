from functions import clear

clear()
print("Title: TBD")
print("\n")
print("1) Play")
print("2) Help")

take_input = True
while take_input:
    input = input("ask something").lower()
    if input in ["help"] or input in [i for i in range(1,2)]: #list of commands and list of acceptable integers
        #vvv Place commands here vvv
        if input in ["help", 2]:
            print("rules of game")
        
    else:
        print("I didn't get that, please try again.")