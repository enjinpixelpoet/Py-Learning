# if = do some code if condition = true
# else it gives false and do some other code

''' age = int(input("What is your age?: "))

if age >= 18 and age <= 100:
    print("You are eligible for Credit Card")
elif age < 0:
    print("You haven't been born yet")
elif age > 100:
    print("You are too old for Credit Card")    
else:
    print("You are not eligible for Credit Card") '''

'''response = input("Would you like food? (Y/N): ")

if response == "Y" or response == "y":
    print("Have some food!")
elif response == "N" or response == "n":
    print("No food for you!")
else:
    print("Invalid response. Please enter Y or N.")'''

'''name = input("What is your name?: ")

if name == "":
    print("You didn't enter a name.")
else:
    print(f"Hello {name}!")'''

'''for_sale = input("Is the item for sale? (Y/N): ")

if for_sale == "Y" or for_sale == "y":
    price = float(input("What is the price of the item?: "))
    print(f"The item is for sale at ${price:.2f}")
else:
    print("The item is not for sale.")'''

online = input("Are you online? (Y/N): ")

if online == "Y" or online == "y":
    print("You are online!")      
