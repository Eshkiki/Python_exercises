# Generate a list of even numbers between 1 and 20 using list comprehension
evens = [ x for x in  range(1,21,1) if x %2 ==0 ]
print(evens)  

# Expected output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
