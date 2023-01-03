# -*- coding: utf-8 -*-

import requests
import json
import pprint

parameter = {
    'site' : 'stackoverflow',
    'sort' : 'votes',
    'order' : 'asc',
    'fromfate' : '2022-12-10',
    'tagged' : 'python',
    'min' : 1
    
    }


r = requests.get("https://api.stackexchange.com/2.3/questions", parameter)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint.pprint(questions)