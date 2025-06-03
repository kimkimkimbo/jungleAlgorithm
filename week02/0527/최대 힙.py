import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            # 음수로 넣었으니까 다시 양수로 출력
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        # 최대 힙처럼 쓰기 위해 음수로 저장
        heapq.heappush(heap, -x)