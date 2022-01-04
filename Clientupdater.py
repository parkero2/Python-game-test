import os
import requests
from os.path import exists
import json
import zipfile

os.system('pip install requests')

def download():
    print(os.system('curl -L https://github.com/parkero2/Python-game-test/archive/refs/heads/main.zip --output file.zip'))
    if (exists('./Python-game-test-main')):
        os.rmdir('./Python-game-test-main')
    with zipfile.ZipFile('./file.zip', 'r') as zip_ref:
        zip_ref.extractall('')
    os.remove('./file.zip')

if exists('./version.json'):
    with open('./version.json') as fil:
        data = json.load(fil)
        if not (json.loads(requests.get('https://raw.githubusercontent.com/parkero2/Python-game-test/main/version.json').content)['version'] == data['version']):
            print("Your version {} is outdated. The latest version is {}. Updating your client.".format(data['version'], json.loads(requests.get('https://raw.githubusercontent.com/parkero2/Python-game-test/main/version.json').content)['version']))
            download()
else:
    print("Downloading game files from remote repository.")
    download()
import client
#if f.readline() != requests.get('')
