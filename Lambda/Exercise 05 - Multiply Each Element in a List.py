# a lambda function to multiply each element in a list by 2.

numbers = [1, 2, 3, 4, 5]
doubled = list(map( (lambda x: x*2), numbers))
print(doubled)  

# Expected output: [2, 4, 6, 8, 10]
