

import sys

n =  int(sys.stdin.readline())

pos = [0] * n #각 열에서 퀸의 위치
flag_a = [False] * n #각 행에 퀸을 배치했는지 체크
flag_b = [False] * (2*n-1) #대각선 방향으로 퀸으로 배치했는지 체크
flag_c = [False] * (2*n-1) #대각선 방향으로 퀸으로 배치했는지 체크


#각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

def put() -> None:
    #각 열에 배치한 퀸의 위치를 출력
    for i in range(n):
        print(f'{pos[i]:2}', end = '')
    print()
    
def set(i: int) -> None:
    #i 열에 퀸을 배치
    for j in range(n):
        if (not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j +(n-1)]):
                pos[i] = j
                if i == (n-1):
                    put()
                
                else:
                    flag_a[j] = flag_b[i+j] = flag_c[i - j + (n-1)] = True
                    set(i+1) #다음 열에 퀸 배치
                    flag_a[j] = flag_b[i+j] = flag_c[i - j + (n-1)] = False

set(0) #0열에 퀸을 배치