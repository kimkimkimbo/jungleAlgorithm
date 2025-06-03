"""
1. 단순 이분탐색
문제:
정렬된 배열이 있을 때, 특정 숫자 x가 배열에 존재하면 "YES", 없으면 **"NO"**를 출력하는 함수를 직접 구현해봐.

예시 입력:
arr = [1, 3, 5, 7, 9, 11, 13]
x = 7

2. 특정 숫자의 인덱스 찾기
문제:
arr 안에서 숫자 x가 처음 등장하는 인덱스를 반환해. 없으면 -1을 반환. (중복 허용)
처음 등장하는 인덱스를 어떻게 알..지..?
음..................... 아!
인덱스 값을 계속 업데이트 하는 거야!
그래서 마지막으로 넘어온 값이 제일 처음 값인 거지
"""

import sys

def Test2(arr, x):
    
    result = -1
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        
        mid = (left + right) // 2
        
        if arr[mid] == x:
            result = mid
            right = mid - 1
            #마지막 위치를 찾을 땐 이렇게!
            #left = mid + 1
        
        elif arr[mid] < x:
            left = mid + 1
        
        elif arr[mid] > x:
            right = mid - 1
    
    return result
        


def Test1(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return "YES"
        
        elif arr[mid] < x:
            left = mid + 1
        
        elif arr[mid] > x:
            right = mid - 1
    
    return "NO"

arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

arr.sort()


#print(Test(arr, x))
print(Test2(arr, x))
    