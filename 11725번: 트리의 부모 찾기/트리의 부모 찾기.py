from collections import deque
import sys

def solve_tree_parent():
    #입력 받기
    n = int(sys.stdin.readline())

    #인접 리스트로 트리 구성
    #graph[i] = i번 노드와 연결된 노드들의 리스트
    graph = [[] for _ in range(n + 1)]

    # n - 1개의 간선 정보 입력
    for _ in range(n - 1):
        num1, num2 = map(int,sys.stdin.readline().split())
        graph[num1].append(num2) #num1과 num2가 연결됨
        graph[num2].append(num1) #양방향 연결

    #각 노드의 부모를 저장할 배열
    parent = [0] * (n + 1) #parent[i] = i번 노드의 부모
    visited = [False] * (n + 1) #방문 여부 확인

    #BFS로 트리 검색 (DFS도 가능)

    # 1단계: 큐에 루트(1) 넣고 시작
    queue = deque([1]) #루트 노드부터 시작
    visited[1] = True # 1번 노드 방문 표시

    while queue:
        # 큐에서 맨 앞의 노드를 꺼내서 current에 저장
        current = queue.popleft()

        #현재 노드와 연결된 모든 노드 확인
        for neighbor in graph[current]:
            if not visited[neighbor]: #아직 방문하지 않은 노드라면
                visited[neighbor] = True
                parent[neighbor] = current #부모 설정
                queue.append(neighbor) # 큐에 추가 (나중에 탐색하기 위해)
    
    #2번 노드부터 N번 노드까지의 부모 출력
    for i in range(2, n + 1):
        print(parent[i])

#실행
solve_tree_parent()



    
