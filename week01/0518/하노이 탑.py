
import sys

"""
n-1개 전까지는 뭐... 재귀함수가 돌아가서 알아서 옮긴거임
n-1까지 끝내면 그 위에 원판들은 다 옮겨진 거니까...
하나만 움직는 거라 끝인 거지.. 응...
"""

n = int(sys.stdin.readline())

#최소 경우의 수 하노이탑 공식 2 n의 제곱 - 1
print(int(2**n -1))

def hanoi(start, aux, end, n):
    #종료 조건 
    if n == 1: #더 이상 쪼갤 필요 없는 최소한의 상황
        print(f'{start} {end}')
        
    else:
        #n-1개까지 임시로 옮간다
        hanoi(start, end, aux, n-1)
        #가장 큰 원판을 ‘도착’으로 옮긴다
        print(f'{start} {end}')
        #임시에서 도착으로 옮긴다
        hanoi(aux, start, end, n-1)
    
#20 이하만 과정 출력    
if n <=20:
    hanoi(1,2,3,n)
