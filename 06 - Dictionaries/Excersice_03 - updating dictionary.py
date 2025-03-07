alice = {"id": 100, "name":"alice" , "scale":7, "point": 36}
employees1 = {"id":[100,101], "name": ["Alice","Bob"], "scale":[7,8], "point": [36, 42]}


alice["point"] = alice["point"] +1
print(alice)
'''
alice.get("scale") = 8
# Ecpected output : SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?'
'''


alice_scale = alice.pop("scale")
print(f"{alice_scale} , {alice}")
# Ecpected output : 7 , {'id': 100, 'name': 'alice', 'point': 37}

del alice["point"]
print(alice)
# Ecpected output : 7 , {'id': 100, 'name': 'alice'}

alice_name = alice.popitem()
print(f"{alice_name} , {alice}")
# Ecpected output : ('name', 'alice') , {'id': 100}

alice = {"id": 100, "name":"alice" , "scale":7, "point": 36}
alice.clear()
print(alice)
# Ecpected output : {}

alice = {"id": 100, "name":"alice" , "scale":7, "point": 36}
alice["salary"] =  36000
print(alice)
# Ecpected value: {'id': 100, 'name': 'alice', 'scale': 7, 'point': 36, 'salary': 36000}

alice = {"id": 100, "name":"alice" , "scale":7, "point": 36}
alice.update({'salary': 36000, 'job': "tutor"})
print(alice)
# Ecpected value: {'id': 100, 'name': 'alice', 'scale': 7, 'point': 36, 'salary': 36000, 'job': 'tutor'}
