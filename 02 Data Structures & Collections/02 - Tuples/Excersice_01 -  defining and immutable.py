# define
my_tuple = (5,2,3,4)
print(my_tuple) 
print(my_tuple[0]) 
print(my_tuple[-1]) 
# Expected output: (5, 2, 3, 4)
#                   5
#                   4

# Changing a value of a tuple
my_tuple = (5,2,3,4)
#my_tuple[0] = 4
# Expected output: TypeError: 'tuple' object does not support item assignment

# mixed values
my_tuple = (5,"string here",3.0,4)
print(my_tuple) 
# Expected output: (5, 'string here', 3.0, 4)

# single value 
single_int = (5)
single_tuple = (5,)

print( type(single_int), single_int)
print( type(single_tuple), single_tuple)

# Expected value: <class 'int'> 5
#                 <class 'tuple'> (5,)


