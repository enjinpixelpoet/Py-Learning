# input() = A function that allows user to enter data.
# It returns a string data type.

name = input("What is your name?: ")
age = input("What is your age?: ")

age = int(age) + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old!")
