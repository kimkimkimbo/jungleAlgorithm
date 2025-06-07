"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

def climbStairs(n):
    #계단 높이가 1이면 경우의 수가 1개
    if n == 1:
        return 1
    
    #계단 높이가 2이면 경우의 수가 2개
    if n == 2:
        return 2
    
    # dp[i]는 i번째 계단에 도달할 수 있는 방법의 수를 의미하므로,
    # dp[n]까지 접근하기 위해 크기를 (n + 1)로 설정
    dp = [0] * (n + 1)


    # 초기 조건: 1번째 계단까지는 1가지, 2번째 계단까지는 2가지
    dp[1] = 1
    dp[2] = 2

    # 점화식: i번째 계단까지의 방법 수 = (i-1)번째 + (i-2)번째까지의 방법 수
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]



print(climbStairs(4))
    