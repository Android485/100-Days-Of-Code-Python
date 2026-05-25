
# Day 7: Complex Control Flow & Game Logic (Hangman)

Welcome to the Day 7 module of my Python portfolio. This milestone focuses on designing state-dependent game loops, coordinating relative data layouts across external source files, implementing bulletproof duplicate-guess verification arrays, and parsing character indexing patterns using linear sequence monitoring.

## 📁 Repository Structure
* `hangman_main.py` - The central execution script containing validation loops, character mapping arrays, and win/loss state evaluators.
* `Hangman_words.py` - An external lexical database storing words utilized during random secret-word generation stages.
* `Hangman_arts.py` - A dedicated visual assets module containing the terminal title ASCII graphic (`logo`) and chronological game lifecycle tracking assets (`stages`).

---

## 🎮 Project: Robust Console Hangman

### Description
An advanced console-based interactive implementation of the classic Hangman guessing game. This iteration replaces volatile counter math with structural array scanning, allowing the codebase to cleanly manage target words featuring duplicate character chains (e.g., repeating vowels or multi-letter patterns) without stalling internal state flags or triggering anomalous win/loss validations.

### Key Features
* **Modular Resource Architecture:** Abstracts graphical art arrays and raw textual vocabularies into distinct modules (`Hangman_arts`, `Hangman_words`) to maintain clean, isolated code separation.
* **Enumerated Linear Scanning:** Leverages Python's native `enumerate()` sequence function to simultaneously capture index pointers and string values, allowing the engine to safely unpack duplicate letters on a single evaluation turn.
* **Global Selection Memory:** Tracks all historical inputs within an isolated `guessed_letters` tracking array, ensuring users are never penalized for repeating previous false choices or locked in redundant validation loops.
* **Defensive Input Enforcement:** Intercepts out-of-bounds characters, number sets, and blank strings via a localized processing checkpoint before committing the token to lifecycle validation blocks.

### How to Run
Ensure that `hangman_main.py`, `Hangman_words.py`, and `Hangman_arts.py` are saved inside the same directory, then execute:
```bash
python3 hangman_main.py

```

---

## 📝 Concepts Learned & Practiced

* Separating development concerns by linking functions across custom module dependencies (`import`).
* Tracking simultaneous index states and string values using `enumerate()` sequence processors.
* Replacing fragile indicator counters with structural checks on active user-facing states (`if "_" not in display_board`).
* Shielding runtime environments from erroneous execution paths by deploying dedicated state verification loops.

```

```