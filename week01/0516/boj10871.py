import sys

num1, num2 = map(int, sys.stdin.readline().split())

arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = []

for i in range(num1):
    if num2 > arr1[i]:
        arr2.append(arr1[i])
        
print(*arr2)