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

def radiation_scenario(stats):
	typing("Over the time you've been in space thus far, \
		you've been exposed to enough radiation to notice bodily changes.")
	if stats["radiation"] < 5:
		typing("Your health is worsening.") #maybe add symptoms of radiation poisoning
	elif stats["radiation"] >= 5:
		typing("However, your powers mani")
	clear()

def enrichment_scenario1():
	clear()
	typing("You have been in your capsule for months now, and you begin to realize that your personal space is being invaded from the small, tight space.")
	

def enrichment_scenario2():
	clear()

def isolation_scenario1():
	clear()

def isolation_scenario2():
	clear()

def starvation_scenario1():
	clear()

def starvation_scenario2():
	clear()