"""
2차원 배열로 문자를 받아서 비교하기??
제일 긴 수열에 길이를 출력
2차원 배열!
테이블로 생각하기 그려보자!
lcs
왼쪽대각선 값이 같을떄..? +1
같이 다르면 왼쪽과 값이 다르면 뢴쪽이나 윗쪽 값 중 제일 큰 값

문자가 같을 때: dp[i][j] = dp[i-1][j-1] + 1
문자가 다를 때 dp[i][j] = max(dp[i-1][j], do[i-1][j-1])
"""

import sys

lineA = list(sys.stdin.readline().strip())
lineB = list(sys.stdin.readline().strip())

dp = [[0] * (len(lineB) + 1) for _ in range(len(lineA) + 1)]


for i in range(len(lineA)):
    for j in range(len(lineB)):
        if lineA[i] == lineB[j]:
            dp[i][j] = dp[i-1][j -1] + 1
        else:
            dp[i][j] = max(dp[i -1][j],dp[i][j-1])


print(max(map(max, dp)))