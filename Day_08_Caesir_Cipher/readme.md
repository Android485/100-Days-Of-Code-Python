
```markdown
# Day 8: Function Parameters & The Caesar Cipher

Welcome to the Day 8 module of my Python portfolio. This milestone focuses heavily on utilizing functions with inputs, distinguishing between positional vs. keyword arguments, executing mathematical string shifts, and mapping multi-conditional algorithms.

## 📁 Repository Structure

- `main.py` - The central execution script for the Caesar Cipher, handling user data loops, shift logic bounds, and terminal IO streams.
- `caeser_art.py` - A dedicated visual assets file containing the custom ASCII branding logo for the cipher engine.
- `life_in_weeks.py` - A chronological utility calculator mapping remaining life targets based on strict age constraints.
- `love_score_calculator.py` - A logical string-parsing script tracking specific character multi-frequencies across custom text profiles.

---

## 🎮 Project 1: Robust Caesar Cipher Engine

### Description

A terminal-based cryptographic tool capable of encoding and decoding text using a positional rotation shift cipher. This implementation isolates the visual elements into a modular component (`caeser_art.py`) and handles classic execution pitfalls—such as shift keys exceeding the native 26-letter alphabetic limit—by applying mathematical modular offsets.

### Key Features

- **Bi-directional Stream Logic:** Consolidates encryption and decryption modules into a singular, flexible execution block utilizing directional parameter flags.
- **Cyclic Index Protection:** Implements modular arithmetic (`shift % 26`) to safely capture arbitrarily large rotational configurations without raising index boundary exceptions.
- **Non-destructive Parsing:** Scans and patches text arrays while completely preserving spaces, integers, and special characters exactly as entered.

### How to Run

```bash
python3 main.py
```

---

## 📅 Project 2: Life in Weeks Calculator

### Description

A mathematical mapping utility demonstrating functional data injection. By accepting a dynamic age input, the script computes a user's current timeline placement against a standardized lifetime target, translating data into days, weeks, and months remaining.

### Key Features

- **Functional Parameters:** Passes real-world tracking variables into custom arithmetic processors.
- **Formatted Console Outputs:** Implements clean Python f-string rendering for structural data presentation.

### How to Run

```bash
python3 life_in_weeks.py
```

---

## 📊 Project 3: Character Frequency Love Score Calculator

### Description

An exercise in advanced string iteration and conditional data manipulation. The script analyzes two distinct string inputs, counts the cumulative occurrences of target characters, and combines those frequencies into a final two-digit statistical score.

### Key Features

- **Case-Insensitive String Sifting:** Standardizes inputs using `.lower()` to eliminate typographical filtering errors.
- **Character Frequency Tracking:** Leverages native string `.count()` methods to systematically evaluate multi-variable character combinations.

### How to Run

```bash
python3 love_score_calculator.py
```

---

## 📝 Concepts Learned & Practiced

- Defining functions with multiple inputs utilizing both positional and keyword schemas.
- Safeguarding array indexes from boundary overflow using modulus loops (`%`).
- Abstracting interface layouts into independent layout modules (`import`).
- Iterating through complex multi-character datasets while preserving structural layouts.
```