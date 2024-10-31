from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))
# idx_list = []
# for i in range(n):
#     idx_list.append(i)

# result = 0
# for idx1, idx2 in list(combinations(idx_list, 2)):
#     if balls[idx1] != balls[idx2]:
#         result += 1

# print(result)

array = [0] * (m+1)
for ball in balls:
    array[ball] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)