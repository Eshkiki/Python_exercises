# removing an item from a list

my_list = [1,2,3,2,4,5,6]

# removing the first item in the list containg 2
my_list.remove(2)  #inplace method
print(my_list)
# Expected output : [1, 3, 4, 5, 6, 7, 8, 9]


# removing a not existing item in the list containg 2
#my_list.remove(0)
print(my_list)

# Expected output : ValueError: list.remove(x): x not in list
'''
To prevent this error
    1. check if the item exists in the list before removing it (using "in" operator or "count" method )
    2. we can use a try-except
    
'''

# remove and return the first item in a list
my_list = [1,2,3,2,4,5,6]
my_list = my_list.pop(0)
print(my_list)
# Expected output : 1

# remove and return the last item in a list
my_list = [1,2,3,2,4,5,6]
my_list= my_list.pop(-1)
print(my_list)
# Expected output : 6

# remove and return the last item in a list
my_list = [1,2,3,2,4,5,6]
my_list= my_list.pop()
print(my_list)
# Expected output : 6
 
'''
pop method is not safe in multi-threaded context
'''