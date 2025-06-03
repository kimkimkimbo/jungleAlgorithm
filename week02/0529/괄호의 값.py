import sys


line = sys.stdin.readline().strip()

stack = []

for c in line:
    if c == '(' or c == '[':
        stack.append(c)
    elif c == ')':
        if stack and stack[-1] == '(':
            stack.pop()
            stack.append(sum(stack)+2)
    elif c == ']':
        if stack and stack[-1] == '[':
            stack.pop()
            stack.append(sum(stack)+2)
#괄호가 쌍을 이루면 스택에 숫자 넣는 거 완료!
#이제 할 일... 스택 안에 숫자 연산해야 함
#괄호 안에 있는 건 걔들끼리 더하기!

