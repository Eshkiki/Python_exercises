# Frozen Sets


my_frozen_set =  frozenset({1,2,3})
print(my_frozen_set)
#Expected output: frozenset({1, 2, 3})



'''
my_frozen_set =  frozenset({1,2,3})
my_frozen_set.add(5)
print(my_frozen_set)
#Expected output: AttributeError: 'frozenset' object has no attribute 'add'
'''


# freezing a set and unfreezing it
my_set = {1,2,3}
my_set.add(4)
my_frozen_set = frozenset(my_set)
print(my_frozen_set)
#Expected output: frozenset({1, 2, 3, 4})
mutable_set = set(my_frozen_set)
mutable_set.add(6)
print(mutable_set)
#Expected output: {1, 2, 3, 4, 6}
