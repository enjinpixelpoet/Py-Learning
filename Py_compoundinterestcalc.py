# Python Compound Interest Calculator

'''principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("Error: Principal amount must be greater than 0")

while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Error: Rate of interest must be greater than 0")

while time <= 0:
    time = float(input("Enter the time: "))
    if time <= 0:
        print("Error: Time amount must be greater than 0")

compound_interest = principle * (1 + rate/100) ** time

print(f"The compound interest is: {compound_interest}") '''

# This has a major flaw, It doesn't accept 0 as a valid input. For that:

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principal amount: "))
    if principle < 0:
        print("Error: Principal amount must be greater than 0")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("Error: Rate of interest must be greater than 0")
    else:
        break

while True:
    time = float(input("Enter the time: "))
    if time < 0:
        print("Error: Time amount must be greater than 0")
    else:
        break

compound_interest = principle * (1 + rate/100) ** time

print(f"The compound interest is: {compound_interest}")