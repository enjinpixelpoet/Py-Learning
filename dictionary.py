# Dictionary = A collection of {key:value} pairs.

capitals = {"USA": "Washington D.C", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}

# print(capitals.get("USA"))
# print(capitals.get("JAPAN"))

# if capitals.get("Japan"):
#    print("That capital exists")
# else:
#    print("That capital does not exist")

# capitals.update({"Germany": "Berlin", "France": "Paris"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("Russia")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# values = capitals.values()
# items = capitals.items()

for key in capitals.keys():
    print(key)
print()
for value in capitals.values():
    print(value)
print()
for item in capitals.items():
    print(item)

for key, value in capitals.items():
    print(f"{key}: {value}")
    

print(capitals.get("USA"))
