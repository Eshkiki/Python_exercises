# unpack a given 3d location to its origin values
location = (10,12,8)
x,y,z = location
print(x,y,z)
# Expected value: 10 12 8


# ignoring one of compnents in a tuple
x1,y1,_ = location
print(x1,y1)
# Expected value: 10 12 



# read multiple values!
try:
    x2,y2 = location
    print(x2,y2)
except Exception as e:
    print(f"An error occurred: {e}")
# Expected value: An error occurred: too many values to unpack (expected 2)

x2, *y2 =  location
print(x2,y2, type(y2)) #the y2 would become a list!, list of values
# Expected value: 10 [12, 8] <class 'list'>




'''
x3, y3, z3, w3 = location
print(x3, y3, z3, w3) 
# Expected value: ValueError: not enough values to unpack (expected 4, got 3)
'''

x3, y3, z3, *w3 =  location
print(x3, y3, z3, w3) 
# Expected value: []


'''
x4, *y4, *z4 =  location
print(x4, *y4, *z4) 
# Expected value: syntaxError: multiple starred expressions in assignment
'''