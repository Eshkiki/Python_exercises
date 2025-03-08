# LifoQueue is not multi-thread safe


from queue import LifoQueue

#empty stack
stack =  LifoQueue(maxsize=2)

#append to right side of queue (end)
stack.put('alice')
stack.put('bob')
print(stack)
# Expected output : deque(['alice', 'bob'])

# Lenghth of Stack
print(stack.qsize())
# Expected output : 2

'''
# append more than capacity
stack.put('jon')
print(stack)
# Expected output : the stack is full, it will wait for empty slot!
'''

try:
    stack.put_nowait('jon')
    print(stack)
except Exception as e:
    print(f"An error occurred: {e}")
# Expected output: put raise Full
 

if not stack.full():
    stack.put('jon')
    print(stack)
# Expected output: 


#read the tem
item = stack.get()
print(item)
# Expected output: bob


item = stack.get()
'''
item = stack.get()
# Expected output : will wait until a job become available
'''
try:
    item = stack.get(timeout=2)
except:
    print("No thing...")
# Expected output :No thing...
 

if not stack.empty():
    item = stack.get()
