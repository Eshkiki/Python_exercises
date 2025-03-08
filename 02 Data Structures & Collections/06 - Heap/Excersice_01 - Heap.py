import heapq

#empty heap
min_heap = []

heapq.heappush(min_heap, 5)
print(min_heap)
heapq.heappush(min_heap, 8)
print(min_heap)
heapq.heappush(min_heap, 3)
print(min_heap)
heapq.heappush(min_heap, 8)
print(min_heap)
heapq.heappush(min_heap, 4)
print(min_heap)

# Expected output: [5]
#                  [5, 8]
#                  [3, 8, 5]
#                  [3, 8, 5, 8]
#                  [3, 4, 5, 8, 8]

# adding an item without maintaining the min_heap properties
min_heap.append(4)
print(min_heap)
# Expected output: [3, 4, 5, 8, 8, 4]
heapq.heapify(min_heap) # the input can be a list as well!
print(min_heap)
# Expected output: [3, 4, 4, 8, 8, 5]


# we dp not have max heap so we can make values negative
max_heap = [-item for item in min_heap]
print(max_heap)
heapq.heapify(max_heap) #inplace!
print(max_heap)
# Expected output: [-3, -4, -4, -8, -8, -5]
#                  [-8, -8, -5, -3, -4, -4]


print(min_heap)
item = heapq.heappop(min_heap) 
print(item, min_heap)
# Expected output: [3, 4, 4, 8, 8, 5]
#                  3 [4, 4, 5, 8, 8]

print(max_heap)
item = -heapq.heappop(max_heap) 
print(item, max_heap)
# Expected output: [-8, -8, -5, -3, -4, -4]
#                  8 [-8, -4, -5, -3, -4]


