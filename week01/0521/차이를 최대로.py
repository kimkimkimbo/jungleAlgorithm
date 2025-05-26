import sys


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

t_list = []

def test(num):
    total = 0

    if num == n:
        return
    
    for i in range(n):
        total += nums[num] - nums[i]
        t_list.append(total)
    
    test(num+1)
    return

test(0)

print(max(t_list))