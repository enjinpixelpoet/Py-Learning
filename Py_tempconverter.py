# Python Temperature Converter

unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
temperature = float(input("Enter the temperature: "))

if unit == "C":
    celsius = temperature
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
elif unit == "F":
    fahrenheit = temperature
    celsius = (temperature - 32) * 5/9
    kelvin = (temperature - 32) * 5/9 + 273.15
elif unit == "K":
    kelvin = temperature
    celsius = temperature - 273.15
    fahrenheit = (temperature - 273.15) * 9/5 + 32
else:
    print("Error: Invalid unit")
    exit()

print(f"Temperature in celsius is {celsius:.2f}°C")
print(f"Temperature in fahrenheit is {fahrenheit:.2f}°F")
print(f"Temperature in kelvin is {kelvin:.2f}°K")