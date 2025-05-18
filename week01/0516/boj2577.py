import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

total = list(map(int, str(a * b * c)))
count = [0] * 10

for t in total:
    if 0 == t:
        count[0] += 1
    elif 1 == t:
        count[1] += 1
    elif 2 == t:
        count[2] += 1
    elif 3 == t:
        count[3] += 1
    elif 4 == t:
        count[4] += 1
    elif 5 == t:
        count[5] += 1
    elif 6 == t:
        count[6] += 1
    elif 7 == t:
        count[7] += 1
    elif 8 == t:
        count[8] += 1
    elif 9 == t:
        count[9] += 1
        
for c in count:
    print(c)    