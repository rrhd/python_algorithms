from collections import deque

queue = deque()

for i in range(10):
    queue.append(i)

print(queue)

queue.popleft()

print(queue)

