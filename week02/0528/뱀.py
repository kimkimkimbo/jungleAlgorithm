#큐
"""
보드 정보
NxN 크기의 정사각형 보드.
좌표는 (0,0)부터 시작하지만, 입력으로는 (1,1)부터 주어진다.
보드의 상하좌우 끝에 벽이 있다 (즉, 벽 충돌은 보드 범위 밖을 벗어나는 경우).

뱀의 초기 상태
시작 위치: 맨 위 맨 좌측 (0, 0)
시작 방향: 오른쪽
시작 길이: 1

게임 규칙 (1초에 한 번씩 진행)
뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
이동한 칸이 다음 중 하나일 경우 게임 종료: 보드 밖 (벽 충돌), 자기 몸과 부딪힘
이동한 칸에 사과가 있으면: 사과를 먹고 꼬리는 움직이지 않음 (길이 +1)
이동한 칸에 사과가 없으면: 꼬리를 한 칸 줄여서 몸 길이는 그대로 유지

방향 전환
방향 전환 횟수: L
각 전환 정보는 X 초 후에 C 방향으로 회전 형식
정수 X와 문자 C
X: 게임 시작 후 지난 시간 (초)
C: 'L'은 왼쪽으로 90도 회전, 'D'는 오른쪽으로 90도 회전
"""
import sys
from collections import deque


N = int(sys.stdin.readline()) #보드의 크기
board = [[0] * N for _ in range(N)]

K = int(sys.stdin.readline()) #사과의 개수

#사과 위치
for i in range(K):
    row, col = map(int,sys.stdin.readline().split())
    board[row-1][col-1] = 1 #사과 위치엔 1



#방향 변환 수
L = int(sys.stdin.readline())

#초, 방향 입력 받기!
turns = [sys.stdin.readline().strip().split() for _ in range(L)]
turns = [(int(X), C) for X, C in turns]
turn_idx = 0 # 현재 turn을 가리키는 인덱스


#리스트 안에 튜플을 넣어야 뱀의 좌표로 쓸 수 있음
snake = deque([(0,0)])

time = 0

direction = 0 #0 = 오른쪽, 1 = 아래, 2 = 왼쪽, 3 = 위
dx = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽, 위
dy = [1, 0, -1, 0] # 오른쪽, 아래, 왼쪽, 위

while True:
    #초!
    time += 1
    
    #현재 머리 위치
    head_x, head_y = snake[-1]
    
    #머리 이동
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]
    
    #벽 충돌 확인 종료 조건 1
    if not (0 <= nx < N and 0 <= ny < N):
        break #0 ~ N-1 까지가 보드 영역 벗어나면 충돌
    
    #자신과 충돌 확인 종료 조건 2
    if (nx, ny) in snake:
        break
    
    #이동 완료~ 머리 추가! [꼬리, 몸통, 머리]
    snake.append((nx, ny))
    
    #사과 있는지 확인!
    if board[nx][ny] == 1:
        board[nx][ny] = 0 #먹은 사과 제거
    else:
        #사과 없다면 꼬리 제거!
        snake.popleft()
    
    #방향 전환
    #index가 L보다 작은지 확인 왜? 방향 전환은 입력받은 수 만큼만 해야 하니까!
    #초와 입력받은 숫자가 같은지 확인! 왜? 1초에 1칸씩이니까 3 D면 3초 흘렀는지 봐야 함
    if turn_idx < L and time == turns[turn_idx][0]:
        if turns[turn_idx][1] == 'L':
            #파이썬에서는 음수를 4로 나누면 양수 나머지를 줌
            direction = (direction - 1) % 4 #L이면 왼쪽 회전
        else:
            direction = (direction + 1) % 4 #오른쪽 회전
        turn_idx += 1 #다음 방향 전환으로 이동

print(time)

