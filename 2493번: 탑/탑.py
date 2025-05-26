import sys

N = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
result = []

for i in range((N-1),-1,-1):
    if tops[i] < tops[i-1]:
        result.append(i)
    elif i == 0:
        result.append(0)
    else:
        for j in range(i-1, -1, -1):
            if tops[i] < tops[j]:
                result.append(j+1)
                break
            elif j == 0:
                result.append(0)

print(*list(reversed(result)))