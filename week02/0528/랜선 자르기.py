import sys

#랜선의 개수 K, 필요한 랜선의 개수 N
K, N = map(int,sys.stdin.readline().split())

#K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이
kList = [int(sys.stdin.readline()) for _ in range(K)]

"""
300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. 
K개의 랜선을 N개로 다 같은 길이로 만들고 싶고, 가지고 있는 랜선의 길이는 Klist
그럼 내가 찾아야 할 건 몇 cm로 잘라야 같은 길이가 되는지?
ㄴㄴ 이 중에서 가장 긴 길이를 찾는 거임
mid 길이로 잘랐을 때 몇 개 나오는지

각 랜선으로 만들 수 있는 조각 수 = 랜선 길이 // mid
L = kList[0] // mid

전체 조각 수 = 위 조각 수들 다 더한 것
total += L

N개 이상 만들어야 하니까
if N <= total: left = mid + 1 else: right = mid - 1

종료 조건, <=인 이유는 마지막 것까지 봐야 하니까
left <= right
"""
left = 1
right = max(kList)
result = 0

while left <= right:
    total = 0 #총 랜선 수
    L = 0  #각 랜선에서 만든 수

    
    mid = (left + right) // 2
    
    for i in range(K):
        L = kList[i] // mid
        total+= L
    
    if N <= total:
        left = mid + 1
        result = mid
    else:
        right = mid -1
        
print(result)