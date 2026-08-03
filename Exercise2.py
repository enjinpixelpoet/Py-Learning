# Exercise 2: Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input(f"What is the price of {item}?: "))
quantity = int(input("How many would you like to buy?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}(s)")
print(f"The total cost is: ${total:.2f}")