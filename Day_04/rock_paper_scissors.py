#!/usr/bin/env python3

import random

rock = '''    Rock
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
      '''

paper = ''' Paper
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)
      '''

scissors = '''Scissors
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
      '''

# Store the art in a matching list order: 0, 1, 2
game_images = [rock, paper, scissors]
options = ["rock", "paper", "scissors"]

# Fool-proof Input Validation Loop
while True:
    try:
        player_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
        player = int(player_input)
        
        if 0 <= player <= 2:
            break  # Input is valid, break the loop and start the game
        print("Invalid number! Please pick 0, 1, or 2.\n")
    except ValueError:
        print("That's not a number! Please enter 0, 1, or 2.\n")

# Assign choices based on index numbers
player_choice = options[player]
computer_choice = random.choice(options)
computer_index = options.index(computer_choice)

# Display the Choices visually using your ASCII art
print("\n--- YOUR CHOICE ---")
print(game_images[player])

print("--- COMPUTER CHOICE ---")
print(game_images[computer_index])

# Game Logic
if player_choice == computer_choice:
    print("It's a draw! Try Again.")

elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("🎉 You win!")

else:
    print("😭 You Lose!")