#!/usr/bin/env python3

import random

numbers = []

# Loop to generate list of 20 random numbers
for i in range(20):
    random_number = random.randint(0, 150)
    numbers.append(random_number)

maximum = numbers[0]

# Loop through the list to find the highest value
for num in numbers:
    if num > maximum:
        maximum = num

print(f"Generated Numbers: {numbers}") 
print(f"The maximum number is {maximum}")