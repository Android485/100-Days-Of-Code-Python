#!/usr/bin/env python3

import random

# List of alphabets, numbers and symbols
alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*'] 

# List comprehensions to gather choices
upper_choices = [random.choice(alphabet_upper) for _ in range(5)]
lower_choices = [random.choice(alphabet_lower) for _ in range(5)]
number_choices = [random.choice(numbers) for _ in range(3)]
symbol_choices = [random.choice(symbols) for _ in range(2)]

# Combine all lists together
combination = upper_choices + lower_choices + number_choices + symbol_choices

#Shuffle the combined list in-place to destroy the predictable pattern
random.shuffle(combination)

# Join and print the secure password
secure_password = "".join(combination)
print(f"Generated Password: {secure_password}")