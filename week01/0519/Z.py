import sys


n, find_r, find_c = map(int,sys.stdin.readline().split())
#arr = [[0 for _ in range(2**n)] for _ in range(2**n)]
i = 0


def Z(r, c, n):
    
    global i, find_r, find_c
    
    #종료 조건
    if n == 1:
        if r == find_r and c == find_c:
            print(i)
            return
        i+=1
        return
    
    Z(r, c, (n // 2))
    Z(r, c+(n // 2), (n // 2))
    Z(r+(n // 2), c, (n // 2))
    Z(r+(n // 2), c+(n // 2), (n // 2))        
        
        
size = 2 ** n
Z(0, 0, size)


