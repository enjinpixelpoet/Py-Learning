# Calculate the Hypotenuse of a Right Triangle
import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

hyp = math.sqrt(pow(a,2) + pow (b,2))

print(f"The length of the hypotenuse is: {round(hyp, 2)} cm")