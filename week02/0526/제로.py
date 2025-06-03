import sys

T = int(sys.stdin.readline())
stack = []

for _ in range(T):
    num = int(sys.stdin.readline().strip())
    
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
        
        
print(sum(stack))