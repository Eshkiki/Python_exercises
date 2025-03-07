# Empty dictionary
my_empty_dict = {}

# Dictionary with values
alice = {"id": 100, "name":"alice" , "scale":7, "point": 36}
print(alice)
# Expected output : {'id': 100, 'name': 'alice', 'scale': 7, 'point': 36}

bob = dict(id = 101, name = "bob", scale = "8", point = 42)
print(bob)
# Expected output : {'id': 101, 'name': 'bob', 'scale': '8', 'point': 42}


employees1 = {"id":[100,101], "name": ["Alice","Bob"], "scale":[7,8], "point": [36, 42]}
print(employees1)
# Expected output : {'id': [100, 101], 'name': ['Alice', 'Bob'], 'scale': [7, 8], 'point': [36, 42]}



nested_dict = {"employee": {"id":[100,101], "name": ["Alice","Bob"], "scale":[7,8], "point": [36, 42]}, "activity": {"id":[100,100,101], "activity_code": [1,2,1]}}
print(nested_dict)
# Expected output : {'employee': {'id': [100, 101], 'name': ['Alice', 'Bob'], 'scale': [7, 8], 'point': [36, 42]}, 'activity': {'id': [100, 100, 101], 'activity_code': [1, 2, 1]}}

nested_dict = {"employee": employees1, "activity": {"id":[100,100,101], "activity_code": [1,2,1]}}
print(nested_dict)
# Expected output : {'employee': {'id': [100, 101], 'name': ['Alice', 'Bob'], 'scale': [7, 8], 'point': [36, 42]}, 'activity': {'id': [100, 100, 101], 'activity_code': [1, 2, 1]}}
