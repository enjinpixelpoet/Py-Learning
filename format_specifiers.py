# Format Specifiers: Used to format the output of a string. {value:flags}

price1 = 32222.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1: ${price1:4}")
print(f"Price 2: ${price2:-}")
print(f"Price 3: ${price3:10}")

# The ones I learnt are:
# , = comma(prints comma in between thousands)
# ._f = decimal point(settles the number of decimal places)
# :, = comma(prints comma in between thousands)
# + = plus sign(puts a plus sign in front of the number if it's positive)
# > = right aligns the number
# < = left aligns the number
# ^ = center aligns the number
