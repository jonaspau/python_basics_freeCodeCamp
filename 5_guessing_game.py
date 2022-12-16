# Guessing game

# Guess a random number between an interval

import random

while True:
    number = random.randint(1,20)
    try:
        guess = int(input("Guess a number: "))
        while guess != number:
            if guess > number:
                print("Guess a smaller number.")
                guess = int(input("Guess again: "))
            else:
                print("Guess a higher number.")
                guess = int(input("Guess again: "))
        else:
            print("Correct")
    except ValueError:
        print("Not a number")
    q = input("Play again (y/n)? ").lower()
    if q[0] == "n":
        break