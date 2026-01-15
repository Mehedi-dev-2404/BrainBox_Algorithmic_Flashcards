import json
import os

flash_file = 'flashcards.json'
data = ""
try:
    with open(flash_file, 'r') as f:
        content = f.read()
        print("file is there")
except FileNotFoundError:
    with open('flashcards.json', "w") as f:
        f.write("[]")

def load():
    data = json.load(flash_file)
    return data

def save(data):
        with open('flashcards.json', "w") as f:
            f.write("{data}")