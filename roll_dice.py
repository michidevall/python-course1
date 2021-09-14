import random

roll = random.randin(1,6)

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print("Correct! Thet rolled a ")