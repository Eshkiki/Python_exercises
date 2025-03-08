# converting tuple to a list
my_tuple = (5,2,3,4)
my_list = list(my_tuple)
print(my_list)
# Expected output:  [5, 2, 3, 4]


# add one item to list and convet the list to tuple
my_list.append(6)
my_tuple = tuple(my_list) 
print(my_tuple)
# Expected output:  (5, 2, 3, 4, 6)
