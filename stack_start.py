#List as stack
stack = []
for i in range(10):
    stack.append(i)

print("Current stack is ")
print(stack)
stack.pop()
print("Popped off last element to get ")
print(stack)
stack.pop(4)
print("Popped off element in index 4 to get ")
print(stack)
