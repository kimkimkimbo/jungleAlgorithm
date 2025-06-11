#부호가 같은 경우 따로 처리 필요 없음

import sys

#55-50+40 -> 55 - (50+40)

expression = sys.stdin.readline().strip()

# '-' 기준으로 나눠서 각 그룹을 만들기
sub_expressions = expression.split('-')


# 각 그룹 내에서 '+' 연산을 먼저 수행
group_sums = []
for sub in sub_expressions:
    nums = list(map(int, sub.split("+")))
    group_sums.append(sum(nums))


# 첫 그룹은 더하고, 나머지는 모두 빼기
result = group_sums[0]
for group in group_sums[1:]:
    result -= group 


print(result)
