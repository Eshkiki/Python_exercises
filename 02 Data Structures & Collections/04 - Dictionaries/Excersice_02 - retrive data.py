alice = {"id": 100, "name":"alice" , "scale":7, "point": 36}
employees1 = {"id":[100,101], "name": ["Alice","Bob"], "scale":[7,8], "point": [36, 42]}

print(alice["id"])
# Expected output: 100

try:
    print(alice["age"])
except Exception as e:
    print(f"An error occurred: {e}")
# Expected output: An error occurred: 'age'


print(alice.get("id"))
# Expected output: 100

print(alice.get("age"))
# Expected output: None

print(alice.get("age", "not found"))
# Expected output: not found

print(alice.keys())
# Expected output: dict_keys(['id', 'name', 'scale', 'point'])

print(alice.values())
# Expected output: dict_values([100, 'alice', 7, 36])

print(alice.items())
# Expected output: dict_items([('id', 100), ('name', 'alice'), ('scale', 7), ('point', 36)])


print(employees1["id"][0])
# Expected output: 100