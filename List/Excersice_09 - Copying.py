my_list = [1,2,3,2,4,5,6]
# assignemnets!

# copy a list

copy_my_list = my_list.copy()
my_list.sort()
print(copy_my_list ==  my_list , copy_my_list ,  my_list)
# Expected output: False [1, 2, 3, 2, 4, 5, 6] [1, 2, 2, 3, 4, 5, 6]

my_list = [1,2,3,2,4,5,6]
copy_my_list = my_list
my_list.sort()
print(copy_my_list ==  my_list, copy_my_list, my_list)
# Expected output: True [1, 2, 2, 3, 4, 5, 6] [1, 2, 2, 3, 4, 5, 6]

# list()
# copy a list
my_list = [1,2,3,2,4,5,6]
copy_my_list = list(my_list)
my_list.sort()
print(copy_my_list ==  my_list , copy_my_list ,  my_list)
# Expected output: False [1, 2, 3, 2, 4, 5, 6] [1, 2, 2, 3, 4, 5, 6]