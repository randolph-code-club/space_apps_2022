from turtle import title
from functions import clear
from functions import typing
import char_creation
import time

clear()
print(r'''
 ____                 ___                                        ___       __  __                         
/\  _`\    __        /\_ \                   __                 /\_ \     /\ \/\ \                        
\ \ \L\ \ /\_\    ___\//\ \     ___      __ /\_\    ___     __  \//\ \    \ \ \_\ \     __   _ __   ___   
 \ \  _ <'\/\ \  / __`\\ \ \   / __`\  /'_ `\/\ \  /'___\ /'__`\  \ \ \    \ \  _  \  /'__`\/\`'__\/ __`\ 
  \ \ \L\ \\ \ \/\ \L\ \\_\ \_/\ \L\ \/\ \L\ \ \ \/\ \__//\ \L\.\_ \_\ \_   \ \ \ \ \/\  __/\ \ \//\ \L\ \
   \ \____/ \ \_\ \____//\____\ \____/\ \____ \ \_\ \____\ \__/.\_\/\____\   \ \_\ \_\ \____\\ \_\\ \____/
    \/___/   \/_/\/___/ \/____/\/___/  \/___L\ \/_/\/____/\/__/\/_/\/____/    \/_/\/_/\/____/ \/_/ \/___/ 
                                         /\____/                                                          
                                         \_/__/    ''')
time.sleep(1)
print("\n")
print("1) Play")
print("2) Help")

title_choice = ""
while title_choice not in ["1", "2", "help", "play"]:
    title_choice = input("\n> ").lower()
if title_choice == "1" or "play":
    clear()
    char_creation.startup()
elif title_choice == "2" or "help":
    clear()
    print("Help TBD")

# take_input = True
# while take_input:
#     input = input("ask something").lower()
#     if input in ["help"] or input in [i for i in range(1,2)]: #list of commands and list of acceptable integers
#         #vvv Place commands here vvv
#         if input in ["help", 2]:
#             print("rules of game")
        
#     else:
#         print("I didn't get that, please try again.")