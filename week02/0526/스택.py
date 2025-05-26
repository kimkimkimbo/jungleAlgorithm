import sys

T = int(sys.stdin.readline())

stack = []

for _ in range(T):
    chat = sys.stdin.readline().strip()
    
    if chat.startswith("push"):
        _, num = chat.split()
        stack.append(num)
    elif chat == "top":
        if stack :
            print(stack[-1])
        else:
            print("-1")
    elif chat == "size":
        print(len(stack))
    elif chat == "empty":
        if stack :
            print(0)
        else:
            print(1)
    elif chat == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)