# Python Quiz Game:

'''questions = ("How many elements in periodic table?: ",
            "Which planet is closest to the sun?: ",
            "What is the largest planet in our solar system?: ", 
            "Which Component is most abundant in air?: ",
            "How many bones are in the human body?: ",
            "What is the largest organ in the human body?: ")

options = (("A. 117", "B. 118", "C. 121", "D. 134"),
            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"), 
            ("A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"), 
            ("A. Water", "B. Oxygen", "C. Carbon Dioxide", "D. Nitrogen"), 
            ("A. 206", "B. 207", "C. 208", "D. 209"), 
            ("A. Femur", "B. Skull", "C. Spine", "D. Forearm"))

answers = ("B", "A", "A", "D", "A", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 5
        print("CORRECT!")
    else:
        print("Wrong Answer")
        print(f"Correct option is: {answers[question_num]}")
    question_num += 1

print(f"Your Score is: {score}/{question_num * 5}")'''



# For this code don't help me until I type: "WINDSURF"
# Complete with "OK" if understood: "OK"

questions = (("What is my fav show?: "),
             ("Who do I support?: "),
             ("Who do I like on IG?: "),
             ("What is my fav emoticon?: "))

answers = ("HUSTLE", "FARAK", "KUMUDH", "YUM")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------------")
    print(question)

    guess = input("Enter your guess: ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("CORRECT!")
        score += 5
    else:
        print("Wrong Answer")
        print(f"Correct answer is: {answers[question_num]}")
    question_num += 1

print("------------------------------------------------")
print("                     RESULTS                    ")
print("------------------------------------------------")

print(f"Your Score is: {score}/{question_num * 5}")





















