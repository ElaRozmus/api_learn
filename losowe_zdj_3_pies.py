# -*- coding: utf-8 -*-

import requests
import json
import webbrowser
from enum import IntEnum


def dogCatBird_func(howManyPictures):
    """This function open a website with a choosen pets( dogs=Shiba, cats, birds)
        Input:
           howManyPictures : int 
        
        Output:
            website
            
   """
   
    parameter = {
        "count" : howManyPictures}
    
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


animalChoice = int(input("""Which animal you choose?:
      1 - Dog
      2 - Cat
      3 - Bird
      
      Place for your decision: """))   #Dog Cat Bird    
      
      
howManyPictures =int(input("How many pictures you want to see?: "))

if animalChoice == whichAnimalEnum.dog:
    dogCatBird_func(howManyPictures)
elif animalChoice == whichAnimalEnum.cat:
    dogCatBird_func(howManyPictures)
elif animalChoice == whichAnimalEnum.bird:
    dogCatBird_func(howManyPictures)
    
