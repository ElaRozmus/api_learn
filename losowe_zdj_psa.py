# -*- coding: utf-8 -*-
import requests
import json
import webbrowser

r = requests.get("https://random.dog/woof.json")

facts = r.json()

for dog in facts:
         webbrowser.open_new_tab(facts['url'])