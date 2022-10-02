from functions import clear
from functions import typing
import char_creation
import time
from game import game

def main():
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

    title_choice = ""
    while title_choice not in ["1", "play"]:
        title_choice = input("\n> ").lower()
    if title_choice == "1" or "play":
        clear()
        stats = char_creation.startup()
        while True:
            print("before game")
            game(stats)
            print("after game")
    elif title_choice == "2" or "help":
        clear()
        print("Help TBD")

if __name__ == '__main__':
    while True:
        try:
            main()
        except ZeroDivisionError:
            pass # you lost