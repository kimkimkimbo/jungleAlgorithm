"""
4. 값이 특정 범위에 있는 원소 개수 세기
문제:
정렬된 배열에서 [l, r] 범위에 있는 값이 몇 개인지 세어라.

예시:
arr = [1, 2, 2, 3, 4, 5, 6, 7]
l = 2
r = 4

정답: 4개 (2, 2, 3, 4)
"""

import sys

def lower(arr, l):
    
    left = 0
    right = len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < l:
            left = mid - 1
        
        else:
            right = mid
        
    return left

def upeer(arr, r):
    left = 0
    right = len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > r:
            right = mid
        else:
            left = mid - 1
    return left

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
l = int(sys.stdin.readline())
r = int(sys.stdin.readline())

print(upeer(arr, r) - lower(arr, l))
