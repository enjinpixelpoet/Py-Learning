# Game of rock paper scissors:

import random

a = random.randint(1, 3)
if a == 1:
    computer = "rock"
elif a == 2:
    computer = "paper"
else:
    computer = "scissors"


while True:
    b = int(input("Enter a choice (1 for rock, 2 for paper, 3 for scissors): "))
    if not b > 3 or  not b < 1:
        pass
    else:
        print("Please enter a valid option")
        continue
    if b == 1:
        player = "rock"
    elif b == 2:
        player = "paper"
    else:
        player = "scissors"

    print(f"Computer's Choice: {computer}")
    print(f"Player's Choice: {player}")

    
    if a == b:
        print("It's a draw!")
    elif (b-a) % 3 == 1:
        print("Player wins!")
    else: 
        print("Computer wins!")
