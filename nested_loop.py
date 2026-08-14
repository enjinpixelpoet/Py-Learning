# nested loop = A loop within another loop

'''for i in range(3):
    for j in range(1,11):
        print(j, end=" ")
    print()'''

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("What symbol would you like to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()