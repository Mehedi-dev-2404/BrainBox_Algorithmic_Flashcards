import json
import os
from datetime import datetime, timedelta

flash_file = 'flashcards.json'
date_now = datetime.now().date()
str_date_now = date_now.strftime("%Y/%m/%d")
three_days = timedelta(days=3)
seven_days = timedelta(days=7)

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

def add_card(data, date_now):
    question = input("Question: ")
    answer = input("Answer: ")

    card_data = {
        "question": question, 
                 "answer": answer, 
                 "level" : 1, 
                 "next_review" : str_date_now
                 }
    data.append(card_data)
    save(data)

def practice(data, date_now, three_days, seven_days, str_date_now):
    cards_to_practice = filter_cards(data, date_now)

    if cards_to_practice:

        for card in cards_to_practice:
            print(f"Question: {card['question']}")
            answer = input("Enter your answer: ")

            if answer == card["answer"]:
                if card["level"] != 3:
                    card["level"] += 1
                print("Correct")

                if card["level"] == 1  :
                    next_review = date_now
                elif card["level"] == 2:
                    next_review = date_now + three_days
                elif card["level"] == 3:
                    next_review = date_now + seven_days
                
                next_review = next_review.strftime("%Y/%m/%d")
                card["next_review"] = next_review
            else:
                card["level"] = 1
                card["next_review"] = str_date_now
                print("Wrong")
            save(data)
            
    else: 
        print("No cards due for review! Go play outside.")


def filter_cards(data, date_now):

    filtered_cards = list()

    for card in data:
        card_date = datetime.strptime(card["next_review"], "%Y/%m/%d").date()
        if card['level'] in [1, 2, 3]:
            if card_date <= date_now:
                filtered_cards.append(card)

    return filtered_cards

def view_stats(data, str_date_now):
    print(f"Total cards: {len(data)}")
    for card in data:
        if card['level'] == 1:
            count_1 += 1
        elif card['level'] == 2:
            count_2 += 1
        elif card['level'] == 3:
            count_3 += 1

        if card["next_review"] == str_date_now:
            due_count += 1

    count_1 = 0
    count_2 = 0
    count_3 = 0
    due_count = 0

    print(f"Level 1 : {count_1}")
    print(f"Level 2 : {count_2}")
    print(f"Level 3 : {count_3}")
    print(f"Due today: {due_count}")

data = load()

while True:
    print("""
1. Add Card
2. Practice
3. View Stats
4. Exit""" )
    operation = int(input("Enter which operation do you want to perform (1-4): "))

    if operation == 1:
        response = add_card(data, date_now)
    elif operation == 2:
        practice(data, date_now, three_days, seven_days, str_date_now)
    elif operation == 3:
        view_stats(data, str_date_now)
    elif operation == 4:
        break