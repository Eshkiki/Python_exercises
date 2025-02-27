# Convert a list of temperatures in Fahrenheit to Celsius using list comprehension.

fahrenheit = [32, 50, 77, 104]
celsius =  [(((x-32)*5)/9) for x in fahrenheit]
print(celsius)  

# Expected output: [0.0, 10.0, 25.0, 40.0]