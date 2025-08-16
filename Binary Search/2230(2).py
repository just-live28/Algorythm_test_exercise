import sys
input = sys.stdin.readline
from bisect import bisect_left
INF = 2 * int(1e9) + 1
# (1) 이분 탐색 방식으로 풀기
# 없는 숫자인 경우, 해당 숫자가 들어갈 가장 왼쪽 idx를 반환

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
    result = INF
    for num in arr:
        idx = bisect_left(arr, num + m)
        if idx < n:
            result = min(result, arr[idx] - num)

    print(result)    