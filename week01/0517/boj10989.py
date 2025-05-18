import sys
#합병정렬 merge sort


t = int(sys.stdin.readline())
nums = []

for i in range(t):
    n = int(sys.stdin.readline())
    nums.append(n)
    

def test(nums):
    #재귀 종료 조건 len(nums) <= 1 각 배열 길이가 1이 될 때까지 쪼개야 하니까
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    
    left = test(nums[:mid])     # 왼쪽: 0 ~ mid-1
    print(left)
    right = test(nums[mid:])    # 오른쪽: mid ~ 끝
    print(right)
    
 



    
#test(nums)
    
    