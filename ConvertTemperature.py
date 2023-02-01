# You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.
# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
# Return the array ans. Answers within 10-5 of the actual answer will be accepted.
# Note that:
# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00

# More readable
def convertTemperature1(celsius): 
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32
    return [kelvin, fahrenheit]

# Faster
def convertTemperature(celsius): 
    return [celsius + 273.15, celsius * 1.80 + 32]

# Test cases
celsius = 36.50
print(convertTemperature(celsius))

celsius = 122.11
print(convertTemperature(celsius))