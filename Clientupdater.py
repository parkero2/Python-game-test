import os
import requests
from os.path import exists
import json

with open('./version.json') as fil:
    data = json.load(fil)
    print(requests.get('https://raw.githubusercontent.com/parkero2/Python-game-test/main/version.py').content)
    data['version']

#if f.readline() != requests.get('')
