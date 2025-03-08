# Find accurance of an item in tuple
my_tuple1 = (5,2,3,4,2,3)
print(my_tuple1.count(7) )
print(my_tuple1.count(2) )
# Expected results: 0
#                   2

# Find index of an element
intrested_value= 2
print(my_tuple1.index(intrested_value))
#Expected output : 1

# Find indces of elemnets!
print([i for i,x in enumerate(my_tuple1) if x == intrested_value])
#Expected outpu : [1, 4]