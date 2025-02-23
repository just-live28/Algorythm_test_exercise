# num - x >= M
# num >= M + x

import sys
input = sys.stdin.readline
from bisect import bisect_left

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

if n == 1:
    print(0)
elif n == 2:
    diff = arr[1] - arr[0]
    if diff >= m:
        print(diff)
    else:
        print(0)
else:
    result = int(2e9) + 1
    for i in range(n):
        idx = bisect_left(arr, arr[i] + m)
        if idx < n:
            result = min(result, arr[idx] - arr[i])

    print(result)