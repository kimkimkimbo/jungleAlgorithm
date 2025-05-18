import sys

t = int(sys.stdin.readline())

for _ in range(t):
    line = sys.stdin.readline().strip().split()
    r = int(line[0])  
    s = line[1]       
    
    result = ""
    for ch in s:
        result += ch * r
    
    print(result)
