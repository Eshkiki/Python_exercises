# removing from a set

my_set =  {3,10,4}

my_set.remove(3)
print(my_set)
#Expected output: 10, 4

'''
my_set.remove(3)
print(my_set)
#Expected output: KeyError: 3
'''

my_set =  {3,10,4}
my_set.discard(3)
print(my_set)
#Expected output: {10, 4}

my_set.discard(3) # does not raise an error when the item does not exsist
print(my_set)
#Expected output: {10, 4}


#remove a random value from set
my_set =  {3,10,4}
item = my_set.pop()

print(f" removed item was {item}, and the set is {my_set}")

#Expected output: removed item was 10, and the set is {3, 4}
'''
Note:   The output might be slightly differents as Sets are unordered collections of unique items.
        Also, pop select a random value!
'''

'''
item = my_set.pop()
item = my_set.pop()
#Expected output: KeyError: 'pop from an empty set'
'''