from itertools import permutations

n, m = map(int, input().split())

arr = list(map(int, input().split()))

for sub_arr in sorted(permutations(arr, m)):
    for i in sub_arr:
        print(i, end=' ')
    print()