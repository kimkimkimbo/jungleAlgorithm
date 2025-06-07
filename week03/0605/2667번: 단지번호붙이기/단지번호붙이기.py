import sys
from collections import deque

N = int(sys.stdin.readline())
Nlist = [] 

#2차원 배열로 받기
for i in range(N):
    temp = list(sys.stdin.readline().strip())
    Nlist.append(temp)

#1인 곳 인덱스만 따로 저장
list = []
for i in range(N):
    for j in range(N):
        if Nlist[i][j] == '1':
            list.append([i,j])

que = deque()

result = []

while list:
    
    que.append(list.pop())

    homecount = 1

    while que:

        c = que.popleft()

        #상하좌우
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        for i in range(4):
            new_r = c[0]+dy[i]
            new_c = c[1]+dx[i]

            if 0 <= new_c < N and 0 <= new_r < N:
                #배열의 최소, 최대 길이 확인
                if [new_r,new_c] in list:
                    que.append([new_r, new_c])
                    list.remove([new_r,new_c])
                    homecount+= 1
        
    result.append(homecount)



print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])