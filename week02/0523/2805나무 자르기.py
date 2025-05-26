import sys
def TreeCut(left, right):
    
    mid = (left + right) // 2
    
    if left > right:
        return right
    
    total = 0
    
    for T in trees:
        if T > mid:
            total += T - mid
    
    if total >= M:
        return TreeCut(mid+1, right)
    
    elif total < M:
        return TreeCut(left, mid-1)
    
    
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

left = 0
right = max(trees)
    
print(TreeCut(left, right))
    
    
