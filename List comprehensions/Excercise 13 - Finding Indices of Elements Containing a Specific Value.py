
# Finding Indices of Elements Containing a Specific Value


my_list = [1,2,3,2,4,5,6]
intrested_value= 2
print([i for i, val in enumerate(my_list) if val == intrested_value])

# Expected value: [1, 3]