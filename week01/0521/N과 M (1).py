import sys


n, m = map(int,sys.stdin.readline().split())
numlist = []

def P(numlist):

    if len(numlist) == m:
        print(*numlist) #*를 붙여서 리스트를 풀어서(print unpacking) 출력하면, 리스트의 요소들이 공백으로 구분되어 한 줄에 출력
        return 

    for i in range(1, n+1):
        if i in numlist:
            continue
        numlist.append(i)
        P(numlist)   
        numlist.pop()
    
P(numlist)