import sys


"""
결국 이진탐색을 두 번 해서, 
target보다 같거나 큰 값이 처음 나오는 위치, 
그리고 target보다 큰 값이 처음 나오는 위치를 찾아서, 
사이의 개수를 빼는 방식이지.
"""
def lower(left, right, nums, target):
    
    #기본 종료 조건
    while left < right:
        
        #mid값 먼저 정하기
        mid = (left + right) // 2
        
        #중간 값이 찾아야 하는 값보다 작으면
        if nums[mid] < target:
            left = mid+1 #시작 인덱스를 미디부터
        else:
            right = mid #아니면 작은 거니까 미디 인덱스를 끝으로 처음부터 찾기
    
    return left #작은 거를 찾는 거니까 시작 인덱스!

def upper(left, right, nums, target):
    
    while left < right:
        
        mid = (left + right) // 2
        
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left

def count(left, right, nums, target):
    return upper(left, right, nums, target) - lower(left, right, nums, target)
        
        
#가지고 있는 숫자 카드의 개수
N = int(sys.stdin.readline())

#숫자 카드에 적혀있는 정수
N_nums = list(map(int,sys.stdin.readline().split()))
N_nums.sort()

#상근이가 가지고 있는지 구해야 하는 숫자 카드의 개수
M = int(sys.stdin.readline())

#숫자 카드에 적혀있는 정수
M_nums = list(map(int,sys.stdin.readline().split()))

left = 0
right = len(N_nums)

result = []
for target in M_nums:
    counts = count(left, right, N_nums, target)
    result.append(str(counts))

print(' '.join(result))