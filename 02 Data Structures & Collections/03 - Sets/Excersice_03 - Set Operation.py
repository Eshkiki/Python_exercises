

#set operation

my_set1 =  {3,10,4}
my_set2 =  {3,6,7}

# Combine two sets
myset = my_set1 | my_set2
print(myset)
#Expected output: {3, 4, 6, 7, 10}

# Find common item in two sets
myset = my_set1 & my_set2
print(myset)
#Expected output:{3}


# Identify elements that exist exclusively in the first set and are absent in the second set.

myset = my_set1 - my_set2
print(myset)
#Expected output: {10, 4}


# Identify elements that exist exclusively in one of sets but not in both. #Xor

myset = my_set1 ^ my_set2
print(myset)
#Expected output: {4, 6, 7, 10} # we do not have 3! here as it is in both of them