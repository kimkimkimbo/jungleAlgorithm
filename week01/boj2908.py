import sys


a, b = sys.stdin.readline().strip().split()

num1 = a[::-1]
num2 = b[::-1]

print(max(int(num1), int(num2)))