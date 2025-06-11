import sys

N = int(sys.stdin.readline())

wine = [int(sys.stdin.readline()) for _ in range(N)]

dp = [0] * (N + 1)

if N == 1:
    print(wine[0])
elif N == 2:
    print(wine[0] + wine[1])
else:
    dp[0] = wine[0] #첫 번째 와인 먹었을 때
    dp[1] = wine[0] + wine[1] #첫 번째 두 번째 와인 먹었을 때

    #연속으로 세 잔은 안 되니까 첫 번째 + 세 번째, 두 번째 + 세 번쨰, #첫 번째 + 두 번째 세 가지 경우 중에서 제일 큰 거
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1]) 
    
    for i in range(3, N):
        dp[i] = max(
        dp[i - 1],
        dp[i - 2] + wine[i],
        dp[i - 3] + wine[i-1] + wine[i]
    )
        
    print(dp[N-1])

