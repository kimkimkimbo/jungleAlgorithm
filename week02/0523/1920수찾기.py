"""
n <- a[n] 몇 개 입력받을 건지
a[n] <- a[n] n 개의 정수
m <- 몇 개 입력받을 걵3ㅣ
b[m] m개의 수
m개의 수가 a[n]에 존재하는지
"""
import sys


def binary_search(nlist, target, start, end):
    
    mid = (start+end) // 2

    #종료조건 
    if start > end:
        return 0
    
    elif nlist[mid] == target:
        return 1
    
    #mid 값보다 클 때
    elif nlist[mid] < target:
        return binary_search(nlist, target, mid + 1, end)
    
    #mid 값보다 작을 때 
    elif nlist[mid] > target:
        return binary_search(nlist, target, start, mid-1)


n = int(sys.stdin.readline())

nlist = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

mlist = list(map(int, sys.stdin.readline().split()))

nlist.sort()

start = 0
mid = len(nlist) // 2
end = len(nlist) -1
    
for target in mlist:
    print(binary_search(nlist, target, start, end))


#시간 초과
# for i in range(m):
#     for j in range(n):
#         if mlist[i] == nlist[j]:
#             result.append(1)
#             break
#         if j == n-1:
#             result.append(0)
#             break

# print(*result)