"""
‘-’와 ‘|’로 이루어진 바닥 장식 모양
두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개 이상은 같은 나무 판자이고, 
두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개 이상은 같은 나무 판자
"""

import sys

#방 바닥의 세로 크기N 가로 크기 M
N, M = map(int,sys.stdin.readline().split())
b = []
for i in range(N):
    line = list(sys.stdin.readline().strip())
    b.append(line)

#print(b)

#방문 체크용
visited = [[False] * M for _ in range(N)]

count = 0

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        
        visited[i][j] = True
        count += 1  # 새 판자 하나 발견
        
        if b[i][j] == '-':
            nj = j + 1
            while nj < M and b[i][nj] == '-' and not visited[i][nj]:
                visited[i][nj] = True
                nj += 1

        elif b[i][j] == '|':
            ni = i + 1
            while ni < N and b[ni][j] == '|' and not visited[ni][j]:
                visited[ni][j] = True
                ni += 1

print(count)

