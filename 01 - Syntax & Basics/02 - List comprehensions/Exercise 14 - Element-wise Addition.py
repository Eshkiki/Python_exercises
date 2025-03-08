# Adding Corresponding Elements of two elements

my_list_1 = [1,2,3,2,4,5,6]
my_list_2 = [10,20,30,20,40,50,60]



elemetwise_sum = [x + y for x, y in zip(my_list_1, my_list_2)]
print(elemetwise_sum)
# Expected results: [11, 22, 33, 22, 44, 55, 66]

# Adding Corresponding Elements of two elements when Unequal-Length
from itertools import zip_longest

my_list_1 = [1,2,3,2,4]
my_list_2 = [10,20,30,20,40,50,60]

elemetwise_sum1 = [x + y for x, y in zip(my_list_1, my_list_2)]
elemetwise_sum2 = [x + y for x, y in zip_longest(my_list_1, my_list_2, fillvalue=0 )]
print(elemetwise_sum1, elemetwise_sum2)
# Expected results: [11, 22, 33, 22, 44] [11, 22, 33, 22, 44, 50, 60]
