# Rock paper scissors game:

import random

print("---x------Rock Paper Scissors Game------x---")

option = random.randint(1, 3)

option2 = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))

while option2 < 1 or option2 > 3:
    print("Invalid choice!")
    option2 = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))


if option == 1:
    print("Computer chooses rock!")
elif option == 2:
    print("Computer chooses paper!")
else:
    print("Computer chooses scissors!")

if option2 == 1:
    print("You choose rock!")
elif option2 == 2:
    print("You choose paper!")
elif option2 == 3:
    print("You chooses scissors!")

if option == option2:
    print("It's a draw!")
elif (option2 - option) == 2 or (option2 - option) == -1:
    print("Computer wins!")
else: 
    print("You win!")

