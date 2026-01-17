# BrainBox — Algorithmic Flashcards (CLI)

BrainBox is a Python command-line flashcard application that implements a simplified spaced repetition system to support efficient and structured learning.

---

## Overview

BrainBox allows users to create flashcards, practice only cards that are due for review, and track learning progress using a level-based system.  
The project focuses on clean logic, persistence, and date-based scheduling rather than UI complexity.

This project was built to strengthen core Python skills and demonstrate practical algorithmic thinking.

---

## Features

- Add flashcards (question and answer)
- Practice only cards that are due for review
- Level-based progression (Levels 1–3)
- Automatic review scheduling
- Persistent storage using JSON
- Progress and statistics screen
- Simple and clean CLI interface

---

## How the Algorithm Works

Each flashcard contains:
- A question
- An answer
- A learning level (1–3)
- A next review date

### Review Logic

| Level | Next Review After Correct Answer |
|------|----------------------------------|
| 1 | Same day |
| 2 | After 3 days |
| 3 | After 7 days |

- Correct answers increase the card’s level
- Incorrect answers reset the card to Level 1
- Only cards with a review date equal to or earlier than today appear during practice

---

## Tech Stack

- Python 3
- JSON (data persistence)
- datetime / timedelta (date scheduling)
- Command-line interface

---

## Project Structure
│
├── brainbox.py
├── flashcards.json
└── README.md

---

## Example Flashcard Format

{
  "question": "What does datetime.now().date() return?",
  "answer": "Today's date",
  "level": 2,
  "next_review": "2026/01/20"
}

---
## Main Menu
<img width="306" height="159" alt="Screenshot 2026-01-17 at 6 02 56 PM" src="https://github.com/user-attachments/assets/ca3877f4-7507-4167-812f-f7d8e60418d4" />

## Practice
<img width="375" height="122" alt="Screenshot 2026-01-17 at 6 04 34 PM" src="https://github.com/user-attachments/assets/419f01a2-37b9-488e-84f7-4b6c70abc1bc" />

## Stats
<img width="170" height="126" alt="Screenshot 2026-01-17 at 6 06 17 PM" src="https://github.com/user-attachments/assets/27bfbf10-7372-431a-8749-ce4156ddd173" />

