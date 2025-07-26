
# 🕹️ Hangman Game

## 📌 Overview
This is a simple **text-based Hangman game** written in Python. The player must guess a randomly selected word one letter at a time, with a limited number of incorrect guesses allowed.

---

## 🚀 Features
- 5 predefined words to guess from
- Input validation for single letters (A–Z)
- Displays current progress and wrong guesses
- Ends with a win or loss message
- Modular functions for clean code design

---

## 🧠 Concepts Used
- `random` and `string` modules
- Sets and loops
- Conditional logic (`if`, `else`)
- Functions
- Console input/output

---

## 🗂️ File Structure
task1.py # Python script with the complete game logic
README.md # Project description and instructions


---

## 🖥️ How to Run
1. Make sure you have **Python 3** installed.
2. Save the code to a file named `task1.py`.
3. Open a terminal or command prompt.
4. Run the script:

```bash
python task1.py

## 📷 Sample Output
=== Hangman ===

Word:  _ _ _ _ _ _
Wrong: 0/6
Pick a letter: p
✅  Good guess!

Word:  p _ _ _ _ _
Wrong: 0/6
Pick a letter: z
❌  Nope!

...

🎉 You won! The word was PLANET.

