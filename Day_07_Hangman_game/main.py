#!/usr/bin/env python3

from hangman_words import word_list
from hangman_arts import stages, logo
import random

chosen_word = random.choice(word_list)
len_chosen_word = len(chosen_word)

# Initialize game states
starter = ["_"] * len_chosen_word
guessed_letters = []  
lives = 6

print(logo)
print(" ".join(starter))

while True:
    player_choice = input("\nGuess a letter: ").lower()

    # Input validation loop
    while True:
        if len(player_choice) != 1 or not player_choice.isalpha():
            print("Invalid input! Please enter a single, valid letter.")
            player_choice = input("Guess a letter: ").lower()
        else:
            break

    #Check if the letter was already guessed before
    if player_choice in guessed_letters:
        print(f"You have already guessed the letter '{player_choice}'. Try a different one.")
        print(" ".join(starter))
        continue  # Skip the rest of the loop and ask for input again
    
    # Track the new valid guess
    guessed_letters.append(player_choice)

    # Scan the entire word for matching positions using a loop
    if player_choice in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == player_choice:
                starter[index] = player_choice
        print(" ".join(starter))
    else:        
        lives -= 1
        print(f"You guessed '{player_choice}', that's not in the word. You lose a life.")
        print(" ".join(starter))
        print(stages[lives])

    # Check win/loss conditions
    if "_" not in starter:
        print("\n**************************** YOU WIN! ****************************")
        break
    elif lives == 0:
        print(f"\n*********************** IT WAS '{chosen_word.upper()}'! YOU LOSE **********************")
        break