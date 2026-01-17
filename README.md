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

```json
{
  "question": "What does datetime.now().date() return?",
  "answer": "Today's date",
  "level": 2,
  "next_review": "2026/01/20"
}
