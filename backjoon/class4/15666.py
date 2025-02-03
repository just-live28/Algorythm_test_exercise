from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

arr = list(combinations_with_replacement(arr, m))
arr.sort()

duplicate = {}
for each in arr:
    if each not in duplicate:
        print(*each)
        duplicate[each] = 1