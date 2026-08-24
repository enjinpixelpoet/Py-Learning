# Keyword arguments = an argument preceded by an identifier

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# hello("hello", "Mr.", last = "James", first = "John")

# for x in range(1, 11):
#     print(x, end= " ")

# print("1","2","3","4","5", sep= "n ")

# Generate phone number

def get_phone(country , area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(91, 123, 456, 7890)

print(phone_num)