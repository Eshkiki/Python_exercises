# Define a set

my_set = {1, "Python", 10, 4, 5}
print(my_set)

#Expected output: {1, 4, 5, 'Python', 10}
'''
the output might be slightly differents as Sets are unordered collections of unique items
'''

my_set =  set()
my_set1 = {}
print(f"using set() -> {type(my_set)} , using {{}} -> {type(my_set1)}")
#Expected output: using set() -> <class 'set'> , using {} -> <class 'dict'>

# adding to a set
my_set =  {3,10,4}
my_set.add(4)
print(my_set)
#Expected output: {10, 3, 4}
my_set.add(1)
print(my_set)
#Expected output: {1, 10, 3, 4}

# add multiple items

my_set =  {3,10,4}
my_set.update([4,10,1,6])
print(my_set)
#Expected output: {1, 3, 4, 6, 10}