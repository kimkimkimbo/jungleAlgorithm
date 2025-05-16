import sys


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    
    def is_prime(n):
        if n < 2:
            return False
    
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        
        return True

    def goldbach(n):
        for i in range(n //2, 1, -1 ):
            if is_prime(i) and is_prime(n-i):
                return (i, n - i)
        
    a, b = goldbach(n)
    print(a,b)