import sys


def Test(Tlist):
    stack = []
    
    for c in Tlist:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return 'NO'
            stack.pop()
    return "YES" if not stack else "NO"


T = int(sys.stdin.readline())

for _ in range(T):
    Tlist= sys.stdin.readline()
    print(Test(Tlist))
    
