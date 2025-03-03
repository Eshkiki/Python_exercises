my_list = [1,2,3,2,4,5,6]


# sorting a list
my_list.sort() # inplace
print(my_list)
# Expected value: [1, 2, 2, 3, 4, 5, 6]

# sorting a list
sorted_list = sorted(my_list)
print(my_list, sorted_list)
# Expected value: [1, 2, 2, 3, 4, 5, 6] [1, 2, 2, 3, 4, 5, 6]

# Reverse a list
print(my_list[::-1])
# Expected value: [6, 5, 4, 2, 3, 2, 1]

# # Reverse a list
my_list.reverse() # inplace
print(my_list)
# Expected value: [6, 5, 4, 2, 3, 2, 1]


# Sort a list ascending
my_list.sort(reverse=False)
print(my_list)
# Expected value: [1, 2, 2, 3, 4, 5, 6]

# Sort a list descending 
my_list.sort(reverse=True)
print(my_list)
# Expected value: [6, 5, 4, 3, 2, 2, 1]