# Default arguments = A default value for certain parameters

def net_price(list_price, discount = 0, tax = 0.05): # It sets a default value if no value is entered
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500, 0.5, 0.05))
# print(net_price(500))
# print(net_price(500, 0.1))

# Count up timer:

import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONEE!")

count(10)