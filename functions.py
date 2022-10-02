import sys
import time
import random
import os

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/100)
	sys.stdout.write("\n")

def clear():
	if sys.platform.startswith("linux"):
		os.system("clear")
	elif sys.platform.startswith("win32"):
		os.system("cls")
	elif sys.platform.startswith("darwin"):
		os.system("clear")

number_lost = 0
def lost_one():
	global number_lost
	number_lost += 1
def count_lost():
	return number_lost

def radiation_scenario(stats):
	clear()
	typing("Over the time you've been in space thus far, you've been exposed to enough radiation to notice bodily changes.")
	#maybe add gameplay effects to certain outcomes?
	#also research the actual effects of radiation, and organisms that resist them (or benefit from them???)
	if stats["radiation"] == 0:
		typing("Due to your radiation resistance level of 0, you are severely affected by the radiation, so much so that you don't know if you can go on.")
		lose()
	elif stats["radiation"] == 10:
		typing("Because of your radiation resistance level of 10, not only do your powers reverse the effects of the radiation, they strengthen because of it.")
	elif stats["radiation"] <= 5:
		typing("You have a radiation resistance level of %s, so your health is worsening." % stats["radiation"]) #maybe add symptoms of radiation poisoning
		lost_one()
	elif stats["radiation"] > 5:
		typing("However, with your radiation resistance level of %s, your powers manifest to reverse the effects of this radiation." % stats["radiation"])

def enrichment_scenario1(stats):
	clear()
	typing("You have been in your capsule for months now, and you begin to realize that your personal space is being invaded from the small, tight space.")
	if stats["enrichment"] == 0: 
		typing("Due to your ease of enrichment level of 0, you are claustrophobic and cannot stand the tight space.")
		lose()
	elif stats["enrichment"] == 10:
		typing("Your ease of enrichment level of 10 causes you be claustrophilic.")
	elif stats["enrichment"] <= 5:
		typing("With an ease of enrichment level of %s, you are extremely uncomfortable in the small space and become worried you won't make it." % stats["enrichment"])
		lost_one()
	elif stats["enrichment"] > 5:
		typing("Because your ease of enrichment level is %s, you don't mind the cramped space and are able to deal with it well." % stats["enrichment"])


def enrichment_scenario2(stats):
	clear()
	typing("Because of the budget cuts, you weren't supplied with any entertainment for your year-long journey.")
	if stats["enrichment"] == 0:
		typing("You are unable to find any form of entertainment for yourself with an enrichment level of 0, and become so bored that you go insane.")
		lose()
	elif stats["enrichment"] == 10:
		typing("You enjoy having nothing to with your enrichment level of 10, and you remain happy throughout your journey.")
	elif stats["enrichment"] <= 5:
		typing("You have an enrichment level of %s, and you can deal with boredom for a limited amount of time." % stats["enrichment"])
		lost_one()
	elif stats["enrichment"] > 5:
		typing("With an enrichment level of %s, you don't have a problem with having nothing to do." % stats["enrichment"])

def isolation_scenario1(stats):
	clear()
	typing("""You've been on this mission for years now. 
	You haven't seen any of the people or things you care about for all of that time, and it's starting to seriously get to you.""")
	if stats["isolation"] == 0:
		typing("""Your loneliness resistance level of 0 causes you to lose all motivation. 
		Even upon arrival to the red planet, all you can do is go home.""")
		lose()
	elif stats["isolation"] == 10:
		typing("However, your loneliness resistance level of 10 seems to increase your determination to complete your mission.")
	elif stats["isolation"] <= 5:
		typing("Although you miss your loved ones on Earth, your loneliness resistance level of %s allows you to push through, with the knowledge that, if you succeed, you will be able to see them again." % stats["isolation"])
		lost_one()
	elif stats["isolation"] > 5:
		typing("""Your loneliness resistance level of %s allows you to enjoy yourself alone. 
		That's not to say you don't miss your loved ones, but you are secure in your knowledge that you'll be able to see them again.""" % stats["isolation"])

def isolation_scenario2(stats):
	clear()
	typing("As you look out into space, you realize just how far away you are from everything you've ever known.")
	if stats["isolation"] == 0:
		typing("Due to your loneliness resistance score of 0, this realization strikes you all at once, and you suddenly become very afraid of doing anything but going back home. Upon arrival on Mars, all you can do is go back home.")
		lose()
	elif stats["isolation"] == 10:
		typing("Due to your loneliness resistance score of 10, this realization only strengthens your desire to succeed so that you can return victorious. You are still able to appreciate the beauty of space.")
	elif stats["isolation"] <= 5:
		typing("Your loneliness resistance score of %s causes your mind to remain troubled by this thought for the rest of your mission. You are all too aware of the risks you are taking to retrieve your wallet." % stats["isolation"])
		lost_one()
	elif stats["isolation"] > 5:
		typing("Your loneliness resistance score of %s allows you to acknowledge this realization without the need to let it occupy your whole mind." % stats["isolation"])

def starvation_scenario1(stats):
	clear()
	typing("As you continue you journey, you realize that you don't have much food with you due to the unfortunate budget cuts.")
	if stats["starvation"] == 0:
		typing("Because your starvation level is 0, you have a huge stomach that you are unable to fill.")
		lose()
	elif stats["starvation"] == 10:
		typing("You have a very small stomach with your starvation level of 10, and eating small rations of food is perfect for you.")
	elif stats["starvation"] <= 5:
		typing("With a starvation level of %s, you hate eating small rations of food, but you have no choice other than dealing with it." % stats["starvation"])
		lost_one()
	elif stats["starvation"] > 5:
		typing("Your starvation level of %s allows you to not have any problem eating small rations of food." % stats["starvation"])

def starvation_scenario2(stats):
	clear()
	typing("As you continue your journey, you realize that you have limited water with you due to the unfortunate budget cuts.")
	if stats["starvation"] == 0:
		typing("Your starvation level is 0, and you can't stand your mouth feeling dry, which prevents you from concentrating.")
		lose()
	elif stats["starvation"] == 10:
		typing("The starvation level of 10 allows your lack of water to push you forward to achieve your goal.")
	elif stats["starvation"] <= 5:
		typing("With a starvation level of %s, you find it very bothersome to ration out your water." % stats["starvation"])
		lost_one()
	elif stats["starvation"] > 5:
		typing("Your starvation level of %s allows you to easily ration out your water." % stats["starvation"])
	
	
def lose():
	print(r'''
 __    __  _____   __  __      __       _____   ____    ____                 
/\ \  /\ \/\  __`\/\ \/\ \    /\ \     /\  __`\/\  _`\ /\  _`\               
\ `\`\\/'/\ \ \/\ \ \ \ \ \   \ \ \    \ \ \/\ \ \,\L\_\ \ \L\_\             
 `\ `\ /'  \ \ \ \ \ \ \ \ \   \ \ \  __\ \ \ \ \/_\__ \\ \  _\L             
   `\ \ \   \ \ \_\ \ \ \_\ \   \ \ \L\ \\ \ \_\ \/\ \L\ \ \ \L\ \__  __  __ 
     \ \_\   \ \_____\ \_____\   \ \____/ \ \_____\ `\____\ \____/\_\/\_\/\_\
      \/_/    \/_____/\/_____/    \/___/   \/_____/\/_____/\/___/\/_/\/_/\/_/
	''')
	typing("Press enter to continue.")
	input("> ")
	raise ZeroDivisionError

def win():
	print(r'''
 /$$     /$$ /$$$$$$  /$$   /$$       /$$      /$$ /$$$$$$ /$$   /$$ /$$ /$$ /$$
|  $$   /$$//$$__  $$| $$  | $$      | $$  /$ | $$|_  $$_/| $$$ | $$| $$| $$| $$
 \  $$ /$$/| $$  \ $$| $$  | $$      | $$ /$$$| $$  | $$  | $$$$| $$| $$| $$| $$
  \  $$$$/ | $$  | $$| $$  | $$      | $$/$$ $$ $$  | $$  | $$ $$ $$| $$| $$| $$
   \  $$/  | $$  | $$| $$  | $$      | $$$$_  $$$$  | $$  | $$  $$$$|__/|__/|__/
    | $$   | $$  | $$| $$  | $$      | $$$/ \  $$$  | $$  | $$\  $$$            
    | $$   |  $$$$$$/|  $$$$$$/      | $$/   \  $$ /$$$$$$| $$ \  $$ /$$ /$$ /$$
    |__/    \______/  \______/       |__/     \__/|______/|__/  \__/|__/|__/|__/
	''')
	typing("Press enter to continue.")
	input("> ")