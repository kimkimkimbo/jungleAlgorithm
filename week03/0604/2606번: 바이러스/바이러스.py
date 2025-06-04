import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    num1, num2 = map(int, sys.stdin.readline().split())
    graph[num1].append(num2)
    graph[num2].append(num1)




def BFS():
    count = 0
    visited = [False] * (N + 1)

    queue = deque([1])
    visited[1] = True
    

    while queue:
        current = queue.popleft()

        for n in graph[current]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)
                count += 1
    
    return count

    

print(BFS())
