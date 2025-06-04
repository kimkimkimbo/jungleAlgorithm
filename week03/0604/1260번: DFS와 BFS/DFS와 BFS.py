import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

#양방향이니까 둘 다 넣어 줌
for _ in range(M):
    num1, num2 = map(int,sys.stdin.readline().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

#작은 값부터니까 정렬!
for arr in graph:
    arr.sort()


def dfs_stack_graph():
    visited = [False] * (N + 1)

    stack = [V]
    result = [] #결과 저장

    while stack:
        current = stack.pop()
        
        if visited[current]:
            continue

        visited[current] = True
        result.append(current)

        for neighbor in reversed(graph[current]):
            if not visited[neighbor]:
                stack.append(neighbor)

    print(*result)

    

def bfs_graph():
    visited = [False] * (N + 1)

    #루트 노드에서 시작해야 하니까 다 V로
    queue = deque([V])
    visited[V] = True 
    result = [] #결과 저장

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    print(*result)


dfs_stack_graph()
bfs_graph()

