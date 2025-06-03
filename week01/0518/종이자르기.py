import sys

w, h = map(int,sys.stdin.readline().split())
num = int(sys.stdin.readline())
line_num = []


for _ in range(num):
    n = map(int,sys.stdin.readline().split())
    line_num.append(list(n))
    #print(line_num)

w_list = [0] * w  
h_cut = []

h_list = [0] * h  
w_cut = []


#print(w_list, h_list)

#w 0 n, h 1 n
for i in range(num):
    
    if 0 == line_num[i][0]:
        #print(line_num[i][0])
        h_cut.append(line_num[i][1])
        #print(line_num[i][1])
        

    elif 1 == line_num[i][0]:
        #print(line_num[i][0])
        w_cut.append(line_num[i][1])
        #print(line_num[i][1])


#길이를 구해야 하니까... 시작과 끝 넣어주기
h_cut = [0] + h_cut + [h]
h_cut.sort()

h_lengths = []
for i in range(1, len(h_cut)):
    h_lengths.append(h_cut[i] - h_cut[i-1])
    #print(h_lengths)
    
w_cut = [0] + w_cut + [w]
w_cut.sort()

w_lengths = []
for i in range(1, len(w_cut)):
    w_lengths.append(w_cut[i] - w_cut[i-1])
    #print(w_lengths)
    
    
print(max(w_lengths) * max(h_lengths))


    
