import sys

# 입력: 첫 줄에 정수의 개수 N
n = int(sys.stdin.readline())

# 두 번째 줄에 n개의 정수가 공백으로 구분되어 주어짐
a = list(map(int, sys.stdin.readline().split()))

# dp[i]는 i번째 원소까지 고려했을 때
# "i번째 원소를 반드시 포함"하는 최대 연속 부분합
dp = [0] * n

# 초기값: 첫 번째 원소 자체로 시작
dp[0] = a[0]

# 결과값 초기화 (전체 dp 중 최댓값을 저장)
max_sum = dp[0]

# 1번째부터 n-1번째까지 반복
for i in range(1, n):
    # 이전 값에 현재 값을 더할지, 아니면 현재 값에서 새로 시작할지 결정
    dp[i] = max(dp[i - 1] + a[i], a[i])
    
    # 지금까지의 최대값 갱신
    max_sum = max(max_sum, dp[i])

# 최종적으로 가장 큰 연속 부분합 출력
print(max_sum)
