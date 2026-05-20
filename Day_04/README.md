# Python Console Games Collection

Welcome to my portfolio repository featuring two interactive, classic console games built using Python. These projects demonstrate fundamental programming concepts including input validation, error handling, lists, structural game logic, and random generation.

## 📁 Repository Structure
* `rock_paper_scissors.py` - A secure, visual implementation of the classic Rock, Paper, Scissors game featuring custom ASCII art.
* `who_will_pay_the_bill.py` - A utility game that randomly selects who pays the restaurant bill from a user-provided list of names.

---

## 🎮 Project 1: Rock, Paper, Scissors

### Description
A clean command-line version of the classic Rock, Paper, Scissors game. This project includes extensive input validation to ensure the program never crashes from unexpected user behavior (such as entering letters or numbers outside the game scope). It also renders descriptive ASCII graphics to visualize player vs. computer choices.

### Key Features
* **Fool-proof Input Handling:** Uses `try/except` blocks to intercept `ValueErrors` gracefully when users submit letters or special symbols instead of numbers.
* **Persistent Loops:** Holds the user within an input prompt cycle until a valid menu selection (`0`, `1`, or `2`) is declared.
* **Consolidated Evaluation Logic:** Implements clean, readable conditional workflows to assess drawing, winning, and losing rules.

### How to Run
```bash
python3 rock_paper_scissors.py


## 🎮 Project 2: Banker Roulette

### Description
A simple mini-game that solves a classic social dilemma: choosing who pays the bill at a dinner gathering. The program accepts a dynamic comma-separated string of names, parses them into a list structure, and leverages pseudo-random selection to pick the target payer.

## 📝 Concepts Learned & Practiced
Catching exceptions using Python try and except frameworks.
Manipulating indices across parallel data arrays and lists.
Working with the Python random standard library suite.
Bypassing manual input crashes through validation checkpoints.

### How to Run
```bash
python3 rock_paper_scissors.py