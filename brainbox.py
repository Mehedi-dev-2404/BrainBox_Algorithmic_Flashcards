import json
import os

flash_file = 'flashcards.json'

try:
    with open(flash_file, 'r') as f:
        content = f.read()
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

def add_card(data):
    load_data = load()
    question = input("Question: ")
    answer = input("Answer: ")
    card_data = {
        "question": question, 
                 "answer": answer, 
                 "level" : 1, 
                 "next_review" : "today"
                 }
    data.append(card_data)
    save(data)

data = load()

while True:
    print("""
1. Add Card
2. Practice
3. View Stats
4. Exit""" )
    operation = int(input("Enter which operation do you want to perform (1-4): "))

    if operation == 1:
        response = add_card(data)
    elif operation == 2:
        pass
    elif operation == 3:
        pass
    elif operation == 4:
        pass
        break

print(data)