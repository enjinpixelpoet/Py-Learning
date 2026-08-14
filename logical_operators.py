# Logical Operators: (or, and, not)
# or = atleast one is true
# and = both is true
# not = inversion

temp = 20
is_sunny = True

if temp >= 28 or is_sunny:
    print("It's a hot day")
elif temp <= 20 and not is_sunny:
    print("It's a cold day")