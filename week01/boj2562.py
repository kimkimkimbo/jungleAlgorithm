import sys

arr1 = []


for i in range(9):
    arr1.append(int(sys.stdin.readline()))

for i in range(len(arr1)):
    if max(arr1) == arr1[i]:
        print(max(arr1))
        print(i+1)