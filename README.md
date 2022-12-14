# BIOLOGICAL HERO
[Click here to play](https://digital-raiders-nasa22.herokuapp.com/)

Biological Hero is a text-based adventure game that simulates the hazardous conditions of space travel. It's a fun way for students to learn the struggles astronauts face.
This is a project for [NASA's Space Apps Challenge 2022](https://www.spaceappschallenge.org/), for the [Biological Superhero challenge](https://2022.spaceappschallenge.org/challenges/2022-challenges/space-biology-superhero/details) (hence the name).

## How to play

[Watch the demo video.](https://www.youtube.com/watch?v=zTIxBmZ4KRU)

In this game, the player creates a biological superhero for the all-important purpose of retrieving your wallet from Mars.
Your character will have 5 stats, based on the [5 Hazards of Human Spaceflight](https://www.nasa.gov/hrp/5-hazards-of-human-spaceflight).
The game interprets these hazards as these 5 biological superpowers:
- resistance to radiation
- ability to be alone and stay mentally healthy
- ability to survive with little nourishment
- ability to retain bodily health in low/no gravity environments
- ease of happiness in otherwise harsh environments
Once your character has been created, you follow them on a mission to Mars with three chapters: on the way, there, and back again.

During character creation, you will have a pool of 25 points to spread throughout the 5 stats, and each stat must stay between 0 and 10. 

<img width="445" alt="image" src="https://user-images.githubusercontent.com/113556883/193467497-c777ac09-564b-4531-8bcf-f6981ed77357.png">

After that, you get to follow your character's journey as they head towards Mars...

![Ignition!](https://user-images.githubusercontent.com/113556883/193467946-cbfdc8f6-ccdd-4fb4-bc2b-e8dec15581ae.gif)

...then arrive on Mars...

<img width="872" alt="image" src="https://user-images.githubusercontent.com/34243402/193467362-8e54bd0b-1d93-4d05-9983-c271bbb5afce.png">

...and finally return to Earth.

screenshot of "you win" screen

## Libraries Used

- [requests](https://pypi.org/project/requests/)
- [terminal-img](https://pypi.org/project/terminal-img/)
- [inquirer](https://pypi.org/project/inquirer/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## APIs Used

- [Mars Photos API](https://github.com/chrisccerami/mars-photo-api) - Used in [chapter 2](https://github.com/randolph-code-club/space_apps_2022/blob/main/level2.py#L24) to give a bit of visual for Mars
- [MAAS2 API](https://maas2.apollorion.com/) - Used in [chapter 2](https://github.com/randolph-code-club/space_apps_2022/blob/main/level2.py#L31) to determine the difficulty of the UV check and to add flavor

## Research Sources

- [NASA's 5 Hazards of Human Spaceflight](https://www.nasa.gov/hrp/5-hazards-of-human-spaceflight)
- [The World Health Organization's Ultraviolet Radiation Index](https://www.who.int/news-room/questions-and-answers/item/radiation-the-ultraviolet-(uv)-index)
