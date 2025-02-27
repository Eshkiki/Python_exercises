# Given a list of numbers, use list comprehension to filter out negative numbers.

numbers = [-10, -5, 0, 5, 10]
positive_numbers =[x for x in numbers if x % 2 ==0 ]
print(positive_numbers)  

# Expected output: [0, 5, 10]