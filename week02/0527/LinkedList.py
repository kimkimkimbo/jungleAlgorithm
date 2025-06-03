#연결 리스트
"""
데이터를 저장할 때 연속된 메모리 공간을 쓰지 않고, 각 노드가 다음 노드의 주소를 가리키는 구조
Python의 list처럼 인덱스로 접근 불가능!

장점 / 단점
중간 삽입/삭제 O(1) 빠름 / 탐색 느림 O(n)
메모리 효율적 / 구현 복잡
"""

#Node 연결 리스트의 기본 단위
class Node:
    def __init__(self, data):
        self.data = data #하나의 데이터를 가짐
        self.next = None #그 다음 노드의 주소를 next에 저장
        
class LinkedList:
    def __init__(self):
        self.head = None #연결 리스트의 처음 노드(시작점)을 의미
        
    def append(self, data):
        new_node = Node(data) #새로운 노드 생성
        
        if not self.head: #비어 있으면 -> 파이썬은 빈 리스트를 F로 구분
            self.head = new_node #head가 없으니 head로 지정
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next #마지막 노드를 찾음
        cur.next = new_node #마지막 노드에 새노드 연결
        
"""
실무에서 사용할 경우
- OS에서 프로세스 관리, 메모리 관리 (리스트의 동적 삽입/삭제가 빠름)
- LRU 캐시 같은 알고리즘 구현할 때 → 가장 최근 사용한 데이터를 앞으로 보내야 함
- 자체 메모리 할당이 필요한 저수준 환경 (C 언어나 시스템 프로그래밍)
"""

"""
리스트(List) / 연결 리스트(Linked List) 차이점
메모리에 연속적으로 저장됨 / 노드가 불연속적으로 저장되고, 각 노드가 다음 노드의 주소를 가짐
빠름 인덱스로 O(1) / 느림 처음부터 순차적으로 찾아야 함 O(n)
중간 삽입/삭제 시 많은 이동 필요 O(n) / 노드 연결만 바꾸면 되므로 빠름 O(1) 단 위치를 찾는 건 O(n)
데이터만 저장 / 데이터 + 포인터(next) 저장하므로 메모리 더 필요
"""
