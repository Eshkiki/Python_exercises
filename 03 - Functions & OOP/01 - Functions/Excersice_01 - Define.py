

def func1():
    print("no parameter, no return")

func1()
#expected output: no parameter, no return

def func2(param1):
    print(f"Parameter value is: {param1}")

func2(4)
#expected output: Parameter value is: 4


def func3(param1):
    return (f"Parameter value is: {param1}")

print(func3(4))
#expected output: Parameter value is: 4

def max(a,b):
    return a if a>b else b
print(max(5, 8))
#expected output: 8


def max(a,b=0):
    return a if a>b else b
print(max(5, 8))
print(max(-5))
#expected output: 8
#                 0

'''
def max(a= 0 , b):
    return a if a>b else b
#expected output: SyntaxError: parameter without a default follows parameter with a default'
'''

def employee_information(name,age):
    print(f" name: {name} age: {age}")

employee_information(age = 23, name = "alice")
#expected output:  name: alice age: 23


def sum_two(a : int , b : int) -> int:
    return a+b

print(sum_two(2,3))
#expected output: 5
