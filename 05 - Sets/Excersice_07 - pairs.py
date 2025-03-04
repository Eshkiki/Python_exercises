# Working with pairs!


myset = {('python',101), ('java', 102), ('c++',201) }
print(myset)
#expected value: {('c++', 201), ('python', 101), ('java', 102)}


myset.add(('python',101))
print(myset)
#expected value: {('c++', 201), ('python', 101), ('java', 102)}
myset.add((101,'python'))
print(myset)
#expected value: {('c++', 201), ('python', 101), (101, 'python'), ('java', 102)}



unique_pair_set = set([tuple(sorted(map(str, x))) for x in myset ]) 
'''
map used because one of our elements was string and otherone was int, otherwise the error would be like: TypeError: '<' not supported between instances of 'int' and 'str
sorted(..) compares elements and sort them
tuple (..) converts pair to tuple from a list
set (..) convert to set from a list
'''
print( unique_pair_set)
#expected value: {('101', 'python'), ('102', 'java'), ('201', 'c++')}

