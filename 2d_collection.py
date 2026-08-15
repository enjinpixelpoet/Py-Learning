# 2D List: List consisting of lists.

# fruits = ["apple", "banana", "cherry","kiwi", "pineapple", "mango"]
# vegetables = ["tomato", "potato", "carrot", "spinach", "broccoli", "cabbage"]
# meats = ["chicken", "beef", "lamb", "pork", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

groceries = [["apple", "banana", "cherry","kiwi", "pineapple", "mango"], ["tomato", "potato", "carrot", "spinach", "broccoli", "cabbage"], ["chicken", "beef", "lamb", "pork", "fish", "turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end= " ")
    print()