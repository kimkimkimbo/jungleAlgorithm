import sys

"""
배열에서 값이 K 이상인 숫자 중에서 가장 작은 수를 출력
첫 줄에 정수 N (1 ≤ N ≤ 100,000)
두 번째 줄에 오름차순 정렬된 N개의 양의 정수
세 번째 줄에 기준값 K (1 ≤ K ≤ 1,000,000,000)
"""


def binary_search_min_ge_k(nList, K, start, end, result):
    
    mid = (start + end) // 2
    
    if start > end:
        return print(result)
    
    if nList[mid] >= K:
        #이 조건이 괜찮은 이유는!!! 정렬되어 있기 때문에!!!
        return binary_search_min_ge_k(nList, K, start, mid - 1, nList[mid])
    else:
        return binary_search_min_ge_k(nList, K, mid + 1, end, result)
    

N = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
r = 0
nList.sort()

binary_search_min_ge_k(nList, K, 0, len(nList) - 1, -1)