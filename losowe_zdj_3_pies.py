# -*- coding: utf-8 -*-

import requests
import json
import webbrowser

howManyPictures =int(input("How many pictures you want to see?: "))
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

# BIRDS
try:
    pictureBirds = animalReguestDict["rBirds"].json()
except json.decoder.JSONDecodeError():
    print("niepoprawny format")
else:
    for dog in pictureBirds:
       webbrowser.open_new_tab(urlDict["urlBirds"])






