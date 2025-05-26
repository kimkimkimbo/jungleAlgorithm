import sys


def T(start, end):
    
    total = 0
    
    #중간값
    mid = mid = (start + end) // 2
    
    #기본 종료 조건
    if start > end:
        return end
    
    for p in nList:
        total+= min(p,mid)
        
    if total > M:
        return T(start, mid-1)
    
    elif total <= M:
        return T(mid+1, end)


N = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

nList.sort()

start = 0
end = max(nList)


print(T(start, end))
    
        
    
    
