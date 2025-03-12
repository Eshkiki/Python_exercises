import timeit

code1 = '''
import random
my_list_1 = [random.randint(1, 100000) for _ in range(10)]
my_list_1.sort()
smallest = my_list_1[:3]
'''

code2 = '''
import random
import heapq
my_list_1 = [random.randint(1, 100000) for _ in range(10)]
heapq.heapify(my_list_1)
smallest = heapq.nsmallest(3, my_list_1)
'''

time1 = timeit.timeit(code1, number=1000)
time2 = timeit.timeit(code2, number=1000)

print(f"Execution time of sort list: {time1:.5f} seconds")
print(f"Execution time of heap: {time2:.5f} seconds")


