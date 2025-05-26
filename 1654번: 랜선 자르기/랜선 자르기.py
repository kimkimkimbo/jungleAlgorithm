import sys

#랜선의 개수 K, 필요한 랜선의 개수 N
K, N = map(int,sys.stdin.readline().split())

#K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이
kList = [int(sys.stdin.readline()) for _ in range(K)]

