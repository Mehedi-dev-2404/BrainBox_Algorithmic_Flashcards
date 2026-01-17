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

def practice(data):
    cards_to_practice = filter_cards(data)

    if cards_to_practice:

        for card in cards_to_practice:
            print(f"Question: {card['question']}")
            answer = input("Enter your answer: ")

            if answer == card["answer"]:
                if card["level"] != 3:
                    card["level"] += 1
                print("Correct")
            else:
                card["level"] = 1
                print("Wrong")
            save(data)
            
    else: 
        print("The card list is empty")


def filter_cards(data):

    filtered_cards = list()

    for card in data:
        if card['level'] in [1, 2, 3]:
            filtered_cards.append(card)
        else:
            print("Level not accepted")

    return filtered_cards

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
        practice(data)
    elif operation == 3:
        pass
    elif operation == 4:
        pass
        break