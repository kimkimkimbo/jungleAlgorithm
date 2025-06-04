import sys
from collections import deque


N, K = map(int,sys.stdin.readline().split())

visited = [False] * 100001

def BFS():
    
    queue = deque()
    queue.append((N, 0)) #현재 위치, 경과 시간 N에 있으면 시작 위치니까 0초!
    #수빈이는 N에 있으니까 N부터 시작
    visited[N] = True

    while queue:
        current, time = queue.popleft() 

        if current == K:
            print(time)
            return
        
        #다음 가능한 이동 위치들
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))




BFS()


