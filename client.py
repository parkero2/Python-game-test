import requests
import os
import json
import threading
import time

session = {
    "GAME" : "",
    "ID" : "",
    "READY" : False
}

def heartbeat():
    beat = requests.post('https://gametest.parkerdev.tk:2053/heartbeat', data={"GAME" : session["GAME"], "ID" : session["ID"]})
    time.sleep(5)

def check_game():
    check = requests.post('https://gametest.parkerdev.tk:2053/check', data={"GAME" : session["GAME"], "ID" : session["ID"]})
    if json.loads(check.text)["PLAYERS"] == 2:
        session["READY"] = True

creategame = False

while creategame != ("C" or "G"):
    creategame = input("Would you like to create a game (C) or join a game (J)?")


if creategame == "C":
    data = requests.get('https://gametest.parkerdev.tk:2053/create')
    print("Your game code is: {}. Waiting for opponent".format(json.loads(data.text)["GAME"]))
    while not session["READY"]:
        check_game()
        time.sleep(1)
    #A second player has connected
