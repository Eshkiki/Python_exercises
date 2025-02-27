# a lambda function to filter out only the odd numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = list(filter( (lambda x: x %2==1), numbers ))
print(odds)  

# Expected output: [1, 3, 5, 7, 9]