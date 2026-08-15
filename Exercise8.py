# Number guessing game

import random

random_num = random.randint(1, 100)

guesses = 0
answer = 0

print("------Python Number Guessing Game------")
while answer != random_num:
    answer = input("Guess a number between 1 and 100: ")
    guesses += 1
    if answer.isdigit():
        answer = int(answer)
        pass
    else:
        print("Please enter a number")
        continue
    if answer < random_num:
        print("Too low!!, try again")

    elif answer > random_num:
        print("Too high!!, try again")
    else:
        print(f"Voila!! {random_num} is the correct answer")

print(f"You got it in {guesses} guesses")
