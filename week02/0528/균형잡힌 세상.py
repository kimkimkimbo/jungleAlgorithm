#모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
#모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
#입력 종료 조건 온점(".")

import sys


def Test(lines):
    stack = []
    
    for c in lines:
        if '(' == c or '[' == c:
            stack.append(c)
        elif ')' == c:
            if not stack or stack[-1] != '(':
                return 'no'
            stack.pop()
        elif ']' == c:
            if not stack or stack[-1] != '[':
                return 'no'
            stack.pop()
        if stack:
            return 'no'
        else:
            return 'yes'

lines = []

while True:
    line = sys.stdin.readline().strip()
    if line == '.':
        break
    lines.append(line)

print(Test(lines))
    
