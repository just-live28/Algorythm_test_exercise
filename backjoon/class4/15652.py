from itertools import combinations_with_replacement

n, m = map(int, input().split())

arr = [x for x in range(1, n+1)]

for each in combinations_with_replacement(arr, m):
    print(*each)