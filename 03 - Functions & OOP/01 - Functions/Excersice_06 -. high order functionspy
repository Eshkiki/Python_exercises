# map
def square(a):
    return a*a
my_list = [1, 2, 3, 4, 5]
print(list(map(square,my_list)))
# Expected output:  [1, 4, 9, 16, 25]

# filter
def is_odd(a):
    return a%2 == 0
print(list(filter(is_odd,my_list)))

# reduce
from functools import reduce
def add(a,b):
    return a + b
intrested_number = 10
my_list = range(intrested_number+1)
print(reduce(add,my_list))

# custom
def my_high_order(func, value):
    sum = 0
    for i in range(value):
        sum = func(sum,value)
    return sum 
result = my_high_order(add, 10)
print(result)
