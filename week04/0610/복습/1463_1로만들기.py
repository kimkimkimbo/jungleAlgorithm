import sys


def make_one(n):

    dp = [0] * (n + 1)

    dp[1] = 0

    for i in range(2, n + 1):
        
        dp[i] = dp[i - 1] + 1

        if n % 2 == 0:
            dp[i] = min(dp[i],dp[i // 2] + 1)
        elif n % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return print(dp[n])


n = int(sys.stdin.readline())

make_one(n)