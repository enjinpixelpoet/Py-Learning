# Logical Operators: (or, and, not)
# or = atleast one is true
# and = both is true
# not = inversion

temp = 39
is_raining = False

if temp > 30 or not is_raining:
    print("It's a hot day")
elif temp <= 30 and is_raining:
    print("It's a raining day")
else:
    print("It's not a hot day")
