# -*- coding: utf-8 -*-
import requests
import json
from enum import IntEnum
import webbrowser

def someFactsDogCat(typeAnimal, animalFactNumber):
    parameter = {
        "amount" : animalFactNumber,
        "animal_type" : typeAnimal
        
        }
    
    r = requests.get("https://cat-fact.herokuapp.com/facts/random", parameter)
    
    try:
        facts_about_animal = r.json()
    except json.decoder.JSONDecodeError:
        print('Niepoprawny format')
    else:
        for animal in facts_about_animal:
            print(animal['text'])


def somePictureDogCat():
    
    
    r = requests.get("https://random.dog/woof.json")
    
    try:
        pictore = r.json()
    except json.decoder.JSONDecodeError:
        print('Niepoprawny format')
    else:
        webbrowser.open_new_tab(pictore['url'])
            
def somePictureDuck():
    
    
    r = requests.get("https://random-d.uk/api/v2/random")
    
    try:
        pictore = r.json()
    except json.decoder.JSONDecodeError:
        print('Niepoprawny format')
    else:
        webbrowser.open_new_tab(pictore['url'])
        


animalEnum = IntEnum("animalEnumXXX", "cat dog")

choiceAnimal = int(input("""If you want random information about cats press 1, about dogs press 2
Please choose which animal you want to see:"""))
animalFactNumber = int(input("Ile faktów chcesz przeczytać?"))

if choiceAnimal == animalEnum.cat:
    someFactsDogCat("cat", animalFactNumber)
    pictureAnimal = input("""Do you want to see the picture of random animal which you chosen?
Please press Yes or No
place for your decision: """).lower()

    if pictureAnimal == "yes":    
        somePictureDuck()
    elif pictureAnimal == "no":
        print("the end")
    else:
        print("""Please write just "yes" or "no" """)
        
elif choiceAnimal == animalEnum.dog:
    someFactsDogCat("dog", animalFactNumber)
    pictureAnimal = input("""Do you want to see the picture of random animal which you chosen?
Please press Yes or No
place for your decision: """).lower()

    if pictureAnimal == "yes":
        somePictureDogCat()
    elif pictureAnimal == "no":
        print("the end")
    else:
        print("""Please write just "yes" or "no" """)
