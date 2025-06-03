N, K = map(int, input().split())
number = input()
stack = []
count = 0


"""
K개를 지워서 큰 숫자를 얻어야 함
스택에 최신값만 비교하는 게 더 효율적이기 때문
pop이 포인트!
정렬 한 번 하고 다 지우면 오래 걸리니까 스택 쓰는 것!
"""
for num in number:
    while stack and count < K and stack[-1] < num:
        stack.pop()
        count += 1
    stack.append(num)

# 내림차순으로 이루어진 숫자의 경우,
# stack[-1] < num 조건에 걸리지 않기 때문에
# 위의 반복문에서 어떤 숫자도 삭제가 되지 못 함
# 하지만 무조건 K개의 숫자를 제거해야하므로, 뒤에서 K개, 또는 남은 개수를 pop() 해야 함
while count < K:
    """
    내림차순, 부분 내림 차순
    5 4 3 2 1
    3 6 1 2
    무조건 K 개 만큼 지워하기 때문에 바로 pop
    """
    stack.pop()
    count += 1

print(''.join(stack))