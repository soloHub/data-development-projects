# Author: Solomon Kareem
# Convert a list of Celsius temperatures to Fahrenheit 
# using a list comprehension

def celsius_to_fahrenheit(celsius):
    return [round(((c * 9 / 5) + 32), 1) for c in celsius]

# Sample Input 1
celsius = [0]
print(celsius_to_fahrenheit(celsius))
# Sample Output 1:
# [32.0]

# Sample Input 2:
celsius = [25, 10, -5]
print(celsius_to_fahrenheit(celsius))
# Sample Output 2:
# [77.0, 50.0, 23.0]