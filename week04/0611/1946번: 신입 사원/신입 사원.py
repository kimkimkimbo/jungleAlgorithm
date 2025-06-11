import sys

T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())
    rank = []

    for i in range(N):
        nums = list(map(int,sys.stdin.readline().split()))
        rank.append(nums)
    
    rank.sort()
    cnt = 1
    passed = rank[0][1]

    for i in range(1, N):
        for j in range(1, 2):
            if passed > rank[i][j]:
                cnt+=1
                passed = rank[i][j]

    print(cnt)