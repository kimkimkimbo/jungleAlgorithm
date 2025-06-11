import sys

N = int(sys.stdin.readline())

def Test(N):

    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        dp = [0] * (N + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, N+1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
        
        return dp[N] 
    

print(Test(N))