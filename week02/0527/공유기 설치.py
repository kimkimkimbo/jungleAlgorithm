#공유기를 설치한 집들끼리 거리
#정렬하고 시작하기
"""
공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 
가장 인접한 두 공유기 사이의 거리는 3이고, 
이 거리보다 크게 공유기를 3개 설치할 수 없다.
mid 최종 값에 후보들
조건을 만족하는 최솟값 혹은 최댓값을 구하는 경우가 많음
조건을 만족해도 최솟값이나 최댓값이 아닐 수 있음
mid로 출력하면 중간에 나갈 수도 있어서 위험!
"""

"""
정렬해야 하면 정렬부터
left, right 값 설정(정렬이 되료ㅜ있는범위)
조건을 생각해보기
left, right 중 정답이 뭔지
left 조건을 만족하는 촤솟값
right 조건을 만족하는 최댓값
"""

import sys


N, C = map(int, sys.stdin.readline().split())
homes = sorted(int(sys.stdin.readline()) for _ in range(N))

left = 1 #최소 거리
right = homes[-1] - homes[0] #최대 거리



result = 0

while left <= right:
    count = 1  # 공유기 설치 개수 (첫 집 설치했으니까 1부터 시작)
    last_installed = homes[0]  # 첫 번째 집엔 무조건 설치!
    
    mid = (left + right) // 2
    
    for i in range(1, N):
        #미디 이상 거리가 되면 설치
        if homes[i] - last_installed >= mid:
            count+= 1
            last_installed = homes[i]
    
    if count >= C:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(result)
    
    
    
