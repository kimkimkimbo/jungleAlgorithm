import sys



def triangle(t, nums):

    dp = []
    for i in range(T):
        dp.append([0] * (i + 1))
    
    dp[0][0] = nums[0][0]

    for i in range(1, t):
        for j in range(len(nums[i])):
            if j == 0: # 맨 왼쪽
                dp[i][j] = dp[i - 1][j] + nums[i][j]
            elif j == i: #맨 오른쪽
                dp[i][j] = dp[i - 1][j - 1] + nums[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + nums[i][j]
    
    return print(max(dp[T-1]))



T = int(sys.stdin.readline())

nums = []
for i in range(T):
    num = list(map(int,sys.stdin.readline().split()))
    nums.append(num)

triangle(T, nums)