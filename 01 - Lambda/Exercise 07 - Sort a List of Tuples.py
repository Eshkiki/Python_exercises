# Sort the following list of tuples based on the second value using sorted() and a lambda function

data = [(1, 3), (2, 2), (3, 1)]
sorted_data = sorted(data, key= lambda x : [x[1], x[0]] )
print(sorted_data)  

# Expected output: [(3, 1), (2, 2), (1, 3)]