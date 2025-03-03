# adding new elements to a list
my_list_1 = list(range(1,10,1)) # 10 is not included!
my_list_1.append(11)
print(my_list_1)

# Expected reults: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]


# inserting two values in a list (at beggining and one before the end)
my_list_1.insert(0,-1)
my_list_1.insert(-1,10)

print(my_list_1)
# Expected reults: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]