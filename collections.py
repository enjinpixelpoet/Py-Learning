# Collection = Single variable that can hold multiple values
# List = A collection which is ordered and changeable. Allows duplicate members. []
# Tuple = A collection which is ordered and unchangeable. Allows duplicate members. {}
# Set = A collection which is unordered, unchangeable*, and unindexed. No duplicate members. ()

# LIST:

# fruits = ["apple", "cherry", "banana", "coconut"]
# print(dir(fruits))
# print(sorted(fruits))
# print(len(fruits))
# fruits[0] = "kiwi"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("cherry"))
# print(fruits.count("cherry"))

# print(fruits[::2])
# for fruit in fruits:
#    print(fruit)


# SET:

# fruits = {"apple", "cherry", "banana", "coconut", "coconut"}

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()

# TUPLES:

fruits = ("apple", "cherry", "banana", "coconut", "coconut")

# print(fruits.count("coconut"))
# print(fruits.index("coconut"))
print("coconut" in fruits)