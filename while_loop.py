# while loop = do something until condition is true

'''age = int(input("What is your age?: "))

while age < 0:
    print("You haven't been born yet")
    age = int(input("What is your age?: "))

print(f"You are {age} years old!")'''


'''food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("Goodbye")'''

num = int(input("Enter a no. between 1 and 10: "))

while num < 1 or num > 10:
    print("Invalid no.")
    num = int(input("Enter a no. between 1 and 10: "))

print(f"You entered {num}")
