from itertools import combinations

n, m = map(int, input().split())

arr = [x for x in range(1, n+1)]

for sub_arr in combinations(arr, m):
    for i in sub_arr:
        print(i, end=' ')
    print()