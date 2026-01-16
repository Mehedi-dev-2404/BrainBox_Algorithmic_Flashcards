import json
import os

flash_file = 'flashcards.json'
data = list()
try:
    with open(flash_file, 'r') as f:
        content = f.read()
        print("file is there")
except FileNotFoundError:
    with open('flashcards.json', "w") as f:
        f.write("[]")

def load():
    with open(flash_file, "r") as f:
        data = json.load(f)
    return data

def save(data):
    with open(flash_file, "w") as f:
        json.dump(data, f)

cards = load()
print(cards)
print(type(cards))