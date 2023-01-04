# -*- coding: utf-8 -*-

import requests
import json
import webbrowser
from enum import IntEnum
def next_level(howManyPictures):
    
    parameter = {
        "count" : howManyPictures
        
        }
    urlDict = {"urlShiba" : "http://shibe.online/api/shibes",
               "urlCats" : "http://shibe.online/api/cats",
               "urlBirds" : "http://shibe.online/api/birds"}
    
    animalReguestDict = {"rshiba" : requests.get(urlDict["urlShiba"], parameter),
                     "rCats" : requests.get(urlDict["urlCats"], parameter),
                     "rBirds" : requests.get(urlDict["urlBirds"], parameter)}
    
    
    #SHIBA
    try:
        pictureShiba = animalReguestDict["rshiba"].json()
    except json.decoder.JSONDecodeError():
        print("niepoprawny format")
    else:
        for dog in pictureShiba:
           webbrowser.open_new_tab(urlDict["urlShiba"])
    #Cats
    try:
        pictureCats = animalReguestDict["rCats"].json()
    except json.decoder.JSONDecodeError():
        print("niepoprawny format")
    else:
        for dog in pictureCats:
           webbrowser.open_new_tab(urlDict["urlCats"]) 
    #birds
    try:
        pictureBirds = animalReguestDict["rBirds"].json()
    except json.decoder.JSONDecodeError():
        print("niepoprawny format")
    else:
        for dog in pictureBirds:
           webbrowser.open_new_tab(urlDict["urlBirds"])

whichAnimalEnum = IntEnum("whichAnimalEnum", "dog cat bird") 


animalChoice = int(input(("""Which animal you choose?:
      1 - Dog
      2 - Cat
      3 - Bird""")))   #Dog Cat Bird        
      
howManyPictures =int(input("How many pictures you want to see?: "))

if animalChoice == whichAnimalEnum.dog:
    next_level(howManyPictures)
elif animalChoice == whichAnimalEnum.cat:
    next_level(howManyPictures)
elif animalChoice == whichAnimalEnum.bird:
    next_level(howManyPictures)
    


