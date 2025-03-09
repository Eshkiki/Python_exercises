# Positional arguments
def employee_information(name,age):
    print(f" name: {name} age: {age}")

myset = ("alice", 20)
employee_information(*myset)
# Expected output:  name: alice age: 20

def employee_information(*info):
    print(f" name: {info[0]} age: {info[1]}")
employee_information("alice", 20)
# Expected output:  name: alice age: 20


# Keyword arguments
def employee_information(**kwargs):
    for key, value in kwargs.items():
        print(f"key {key} : value {value}")
employee_information(name='Alice')
# Expected output:  key name : value Alice

mydict = {"name":'Alice', 'age': 30}
employee_information(**mydict)
# Expected output:  key name : value Alice
#                   key age : value 30

employee_information(name='Alice', age= 30)
# Expected output:  key name : value Alice
#                   key age : value 30


def both_type_func(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

both_type_func(myset,**mydict )
# Expected output:  Positional arguments: (('alice', 20),)
#                   Keyword arguments: {'name': 'Alice', 'age': 30}