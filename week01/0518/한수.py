import sys

x = int(sys.stdin.readline())


def test(x):
    count = 0
    
    for i in range(1, x+1):
        
        if i <= 99:
            count+=1
            
        elif i < 1000:
            a = (i // 100) % 10
            b = (i // 10) % 10
            c = i % 10
            
            if b - a == c - b:
                count+=1
        
        
            
    print(count)


test(x)