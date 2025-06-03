import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

count = 0
for num in nums:
    if is_prime(num):
        count += 1

print(count)
