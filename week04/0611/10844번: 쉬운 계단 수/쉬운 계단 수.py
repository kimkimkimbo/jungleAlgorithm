import sys

N = int(sys.stdin.readline())
MOD = 1000000000

# dp[n][d] = 길이가 n이고 마지막 숫자가 d인 계단수의 개수
dp = [[0] * 10 for _ in range(N + 1)]

# 길이가 1일 때 초기값 설정 (0은 제외, 문제 조건)
for d in range(1, 10):
    dp[1][d] = 1

# 길이가 2 이상일 때 점화식 적용
for n in range(2, N + 1):
    for d in range(10):
        if d == 0:
            dp[n][d] = dp[n - 1][1]
        elif d == 9:
            dp[n][d] = dp[n - 1][8]
        else:
            dp[n][d] = dp[n - 1][d - 1] + dp[n - 1][d + 1]
        dp[n][d] %= MOD  # 모듈러 연산 꼭 해줘야 함!

# 길이가 N인 계단수 개수는 마지막 자리 0~9 모두 합친 것
print(sum(dp[N]) % MOD)
