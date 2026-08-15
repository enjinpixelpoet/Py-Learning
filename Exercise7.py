# 2D Keypad:

keypad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for rows in keypad:
    for columns in rows:
        print(columns, end = " ")
    print()
        

