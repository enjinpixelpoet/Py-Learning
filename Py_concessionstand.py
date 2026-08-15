# Concession stand program

menu = {"Pizza": 10.99, "Burger": 5.99, "Fries": 3.99, "Soda": 2.99, "Water": 1.99}

cart = []
total = 0
print("---------MENU---------")
for key, value in menu.items():
    print(f"{key:7}: ${value:.2f}")
print("----------------------")

while True:
    food = input("Select an item (q to quit): ").capitalize()
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------Your Order------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total is ${total:.2f}")