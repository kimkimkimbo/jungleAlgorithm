import sys

N, K = map(int,sys.stdin.readline().split())
coins = []

for i in range(N):
    coin = int(sys.stdin.readline())
    coins.append(coin)

coins.reverse()
cnt = 0

for coin in coins:
    cnt += K // coin
    K = K % coin

print(cnt)