import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    chat = sys.stdin.readline().strip()
    
    if chat.startswith("push"):
        _, num = chat.split()
        queue.append(num)
    elif chat == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif chat == 'size':
        print(len(queue))
    elif chat == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif chat == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif chat == 'back':
        print(queue[-1]) if queue else print(-1)
        