import sys

def triangle(nums, T):

    dp = []
    for i in range(T):
        dp.append([0] * (i + 1))

    dp[0][0] = nums[0][0]

    for i in range(1,T):
        for j in range(len(nums[i])):
            if j == 0:  # 맨 왼쪽 - 바로 위에서만 올 수 있음
                dp[i][j] = dp[i-1][j] + nums[i][j]
            elif j == i:  # 맨 오른쪽 - 왼쪽 위에서만 올 수 있음
                dp[i][j] = dp[i-1][j-1] + nums[i][j]
            else:  # 중간 - 두 곳에서 올 수 있음, 최대값 선택
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + nums[i][j]
    
        
    return max(dp[T-1])


T = int(sys.stdin.readline())
Tlist = []  # 빈 리스트로 초기화

for _ in range(T):
    num = list(map(int, sys.stdin.readline().split()))  # map을 list로 변환
    Tlist.append(num)

#print(Tlist)

print(triangle(Tlist, T))