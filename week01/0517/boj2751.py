import sys

t = int(sys.stdin.readline())
nums = []

for i in range(t):
    n = int(sys.stdin.readline())
    nums.append(n)

nums.sort()

print('\n'.join(map(str, nums)))


# for i in range(t):
#     for j in range(t - i -1):
#         if nums[j] > nums[j+1]:
#            temp = nums[j]
#            nums[j] = nums[j+1]
#            nums[j+1] = temp
# print(nums)



# for i in range(t):
#     for j in range(t):
#        if nums[i] < nums[j]:
#            temp = nums[i]
#            nums[i] = nums[j]
#            nums[j] = temp