import sys

testnum = int(sys.stdin.readline())

for i in range(testnum):
    avg = 0
    score = []
    
    score = list(map(int, sys.stdin.readline().split()))
    
    for i in range(score[0]):
        avg += score[i+1]
    
    avg = avg / score[0]
    
    count = 0
    
    for s in score[1:]:
        if s > avg:
            count += 1
    
    print(f"{count/score[0]*100:.3f}%")        
    
        