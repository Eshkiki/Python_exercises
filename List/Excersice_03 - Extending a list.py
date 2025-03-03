# Merge two lists by extending one list with the elements of the other, appending all items from one list to the end of the other.
my_list_1 = [1,2,3,4,5]
my_list_2 = list(range(6,10,1))

extended_list_1 =my_list_1 + my_list_2

extended_list_2 = my_list_1
extended_list_2.extend( my_list_2) # note: extend method is inplace method and does not return anything, it will apply changes to the first list directly

print(extended_list_1, extended_list_2)

# Expected output : [1, 2, 3, 4, 5, 6, 7, 8, 9] [1, 2, 3, 4, 5, 6, 7, 8, 9]