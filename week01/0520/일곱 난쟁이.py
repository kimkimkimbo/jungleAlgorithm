import sys


h, findvalue = [],[]
total = 0

for _ in range(9):
    n = int(sys.stdin.readline())
    h.append(n)


total = sum(h)
i = 0

def find(h, total, i):
    
    if i >= (len(h) -1):
        return
    
    for j in range(i+1,len(h)):
        if (total -(h[i]+h[j])) == 100:
            return (h[i],h[j])
        
    return find(h, total, i + 1)

findvalue = find(h, total, 0)

h.sort()
#print(findvalue)


for i in range(len(findvalue)):
    for j in range(len(h)):
        if findvalue[i] == h[j]:
            h.remove(h[j])
            break
        
for x in h:
    print(x)
    

            
            
#def find_2(total, h, n, i):
    
#     if n <= 1:
#         return

    
#     if (total -(h[i]+h[i+1])) == 100:
#         total-= (h[i]+h[i+1])

#         find.append(h[i])
#         find.append(h[i+1])       
#         return find

    
#     find_2(total, h, n-1, i+1)
    
    
# find_2(total, h, len(h),i)            
            
# for i in  range(len(h)):
#     if (total -(h[i]+h[i+1])) == 100:
#         total-= (h[i]+h[i+1])

#         find.append(h[i])
#         find.append(h[i+1])        
#         break
        