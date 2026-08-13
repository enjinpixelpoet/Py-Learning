# Python Weight Converter

weight = float(input("Enter the weight: "))
unit = input("Enter the unit (kg, g, lb, oz): ").lower()


if unit == "kg":
    weight_in_kilograms = weight
    weight_in_grams = weight * 1000
    weight_in_pounds = weight * 2.205
    weight_in_ounces = weight * 35.274
elif unit == "g":
    weight_in_grams = weight
    weight_in_kilograms = weight / 1000
    weight_in_pounds = weight * 0.002205
    weight_in_ounces = weight * 0.035274
elif unit == "lb":
    weight_in_pounds = weight
    weight_in_kilograms = weight / 2.205
    weight_in_grams = weight * 453.592
    weight_in_ounces = weight * 16
elif unit == "oz":
    weight_in_ounces = weight
    weight_in_kilograms = weight / 35.274
    weight_in_grams = weight * 28.3495
    weight_in_pounds = weight / 16
else:
    print("Error: Invalid unit")
    exit()



print(f"Weight in kilograms: {weight_in_kilograms:.2f} kg")
print(f"Weight in grams: {weight_in_grams:.2f} g")
print(f"Weight in pounds: {weight_in_pounds:.2f} lb")
print(f"Weight in ounces: {weight_in_ounces:.2f} oz")