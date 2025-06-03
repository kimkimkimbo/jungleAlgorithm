import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
que = deque()

for i in range(1, N+1):
    que.append(i)

p = K - 1
r = []
while True: 
    if p == 0:
        print("<"+", ".join(map(str, que))+">")
        break
    
    elif len(que) <= 0:
        print("<"+", ".join(map(str, r))+">")
        break
    
    else:
        for i in range(p):
            que.append(que[0])
            que.popleft()
        
        r.append(que[0])    
        que.popleft()

