
#[new_expression for variable in iterable if 조건]


arr = [1, 2, 3, 4, 5]
t = [x  for x in arr]
print(t)

arr = [1, 2, 3, 4, 5]
t = [x * x for x in arr]
#arr 안에 있는 x들을 하나씩 꺼내서, 각각 x * x 한 결과를 리스트로 만들어 줘.
print(t)


t = [x * x for x in arr if x > 1]
#arr 안에 있는 x들을 하나씩 꺼내서, 각각 x > 1 조건을 만족하면 x * x 한 결과를 리스트로 만들어 줘.
print(t)