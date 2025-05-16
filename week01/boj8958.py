import sys

num = int(sys.stdin.readline())
score = []
    
for i in range(num):
    total = 0
    combo = 0

    
    a = list(sys.stdin.readline().strip())
    #print(a)
    
    for i in range(len(a)):
        if "O" == a[i]:
            combo+=1
            total += combo
            
        elif "X" == a[i]:
            combo = 0
    
    score.append(total)
    
   
for s in score:
    print(s)