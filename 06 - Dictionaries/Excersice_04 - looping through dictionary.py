alice = {"id": 100, "name":"alice" , "scale":7, "point": 36}
employees1 = {"id":[100,101], "name": ["Alice","Bob"], "scale":[7,8], "point": [36, 42]}

# keys
for key in alice:
    print(key)
# Expected values: id
#                  name
#                  scale
#                  point
print('--------')
for key in alice.keys():
    print(key)
# Expected values: 100
#                  alice
#                  7
#                  36
print('--------')

# values
for value in alice.values():
    print(value)
print('--------')
# items
for item in alice.items():
    print(item)
# Expected values: ('id', 100)
#                  ('name', 'alice')
#                  ('scale', 7)
#                  ('point', 36)
print('--------')
# Iterate through each row and print the values
for i in range(len(employees1['id'])):
    row = {key: employees1[key][i] for key in employees1}
    print(row)
# Expected values: {'id': 100, 'name': 'Alice', 'scale': 7, 'point': 36}
#                  {'id': 101, 'name': 'Bob', 'scale': 8, 'point': 42}
 



