# collections.deque is not multi-thread safe

from collections import deque

#empty stack
stack = deque()

#append to right side of queue (end)
stack.append('alice')
stack.append('bob')
print(stack)
# Expected output : deque(['alice', 'bob'])

# Lenghth of Stack
print(len(stack))
# Expected output : 2

# append to left side of queue (start)
stack.appendleft('jon')
print(stack)
# Expected output : deque(['jon','alice', 'bob'])


#read the first item
print(stack[0])
# Expected output : 'jon'

#read the last item
print(stack[-1])
# Expected output : 'bob'

# read and remove from right (pop the last one)
item = stack.pop()
print(item, stack)
# Expected output : 'bob' deque(['jon', 'alice'])

# read and remove from right (pop the first one)
stack.append('bob')
item = stack.popleft()
print(item, stack)
# Expected output : jon deque(['alice', 'bob'])

