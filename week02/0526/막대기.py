import sys

N = int(sys.stdin.readline())
stack = []
maxH = []
c = 0

nums = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]


#입력 순서 뒤집기
#오른쪽에서 왼쪽으로 비교
#가장 큰 높이보다 크면 보인다.
#현재까지 본 것 중에서 가장 높은 막대기보다 높아야 보인다.
#같거나 작으면 가려진다.

for h in reversed(nums):
    if h > maxH:
        maxH = h
        c += 1

print(c)