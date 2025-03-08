import heapq
priority_queue = []

heapq.heappush(priority_queue, (10, 't1'))
heapq.heappush(priority_queue, (4, 't2'))
heapq.heappush(priority_queue, (6, 't1'))
heapq.heappush(priority_queue, (5, 't3'))
heapq.heappush(priority_queue, (4, 't1'))
heapq.heappush(priority_queue, (8, 't2'))



print(heapq.heappop(priority_queue))  
print(heapq.heappop(priority_queue))  
print(heapq.heappop(priority_queue))  