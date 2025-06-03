import sys

N = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
result = [0] * N
stack = []  # (index, height)

for i in range(N):
    while stack and stack[-1][1] < tops[i]:
        stack.pop()
    
    if stack:
        result[i] = stack[-1][0]
        
    stack.append((i+1, tops[i]))

print(*result)
    


#시간 초과!
# for i in range((N-1),-1,-1):
#     if tops[i] < tops[i-1]:
#         result.append(i)
#     elif i == 0:
#         result.append(0)
#     else:
#         for j in range(i-1, -1, -1):
#             if tops[i] < tops[j]:
#                 result.append(j+1)
#                 break
#             elif j == 0:
#                 result.append(0)

# print(*list(reversed(result)))