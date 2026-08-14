# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ").capitalize()
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)
        total += price

print("----- YOUR CART -----")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")

print(f"Total: ${total:.2f}")
