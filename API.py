# -*- coding: utf-8 -*-

import requests
import json
import webbrowser

from datetime import datetime, timedelta
# %%
timeBefore = timedelta(days = 7)
searchTime = datetime.today() - timeBefore

# %%
parameter = {
    'site' : 'stackoverflow',
    'sort' : 'votes',
    'order' : 'desc',
    'fromdate' : int(searchTime.timestamp()),
    'tagged' : 'python',
    'min' : 10
    
    }


r = requests.get("https://api.stackexchange.com/2.3/questions", parameter)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions['items']:
        webbrowser.open_new_tab(question['link'])
    