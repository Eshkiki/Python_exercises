
my_list = list(range(1,10,1))
# Find the length of a list
print(f" The length of our list is {len(my_list)}")

# Expected output: "The length of our list is 9 "


# print the first item in a list
print(f"The first item in the cell is {my_list[0]}")
# Expected output: "The first item in the cell is 1"

#print the last item in a list
print(f"The last item in the cell is {my_list[-1]}")
last_item  = len(my_list)-1
print(f"Finding he last item in the cell with len! {my_list[last_item]} ")
# Expected output: "The last item in the cell is 9
#                   Finding he last item in the cell with len! 9"



# Display elements in a list from the 4th to the 6th position inclusive
print(my_list[3:5])
# Expected output: [4, 5]

# Display elements in a list starting from the 4th position to two items before the end
print(my_list[3:-2])
# Expected output: [4, 5, 6, 7]


# Display all elements in a list up to the 6th position
print(my_list[:5])
# Expected output: [1, 2, 3, 4, 5]


# Display elements in a list starting from the 6th position to the end
print(my_list[5:])
# Expected output: [6, 7, 8, 9]

# Given a list ranging from 1 to 10, display all odd numbers it contains
print(my_list[::2])
# Expected output: [1, 3, 5, 7, 9]

# Given a list ranging from 1 to 10, display all even numbers it contains
print(my_list[1::2])
# Expected output: [2, 4, 6, 8]
  