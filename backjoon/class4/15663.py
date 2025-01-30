# n개의 자연수에서 m개를 고른 순열(중복 수열 x)
from itertools import permutations

n, m = map(int, input().split())
array = list(map(int, input().split()))

result = []
for each in permutations(array, m):
    result.append(each)

result = list(set(result))
result.sort()

for each in result:
    print(*each)