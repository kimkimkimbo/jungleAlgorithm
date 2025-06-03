"""
3. 숫자의 등장 횟수
문제:
정렬된 배열에서 어떤 숫자 x가 몇 번 나오는지 세는 함수를 만들어봐.
👉 lower_bound, upper_bound 아이디어 직접 구현

예시:
arr = [1, 2, 2, 2, 3, 4]
x = 2  # → 3번 등장
"""

import sys

def lower_bound(arr, x):
    left = 0
    right = len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] >= x:
            right = mid

        elif arr[mid] < x:
            left = mid + 1
            
    return left


def upper_bound(arr, x):
    left = 0
    right = len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] <= x:
            left = mid + 1
        
        elif arr[mid] > x:
            right = mid
            
    return left

arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

arr.sort()

print(upper_bound(arr, x) - lower_bound(arr, x))