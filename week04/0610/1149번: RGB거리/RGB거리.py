import sys

N = int(sys.stdin.readline())
colors = []

#colors[n][0] 빨강, colors[n][1] 초록, colors[n][2] 파랑
for _ in range(N):
    color = list(map(int,sys.stdin.readline().split()))
    colors.append(color)

def RGBmin(n, colors):

    dp = [[0] * 3 for _ in range(n)]

    dp[0] = colors[0]

    for i in range(1, n):
        dp[i][0] = colors[i][0] + min(dp[i - 1][1],dp[i - 1][2])
        dp[i][1] = colors[i][1] + min(dp[i - 1][0],dp[i - 1][2])
        dp[i][2] = colors[i][2] + min(dp[i - 1][0],dp[i - 1][1])
    
    return min(dp[n - 1])

print(RGBmin(N, colors))