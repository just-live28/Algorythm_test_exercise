# 공유기 사이 거리를 mid로 놓았을 때, c개 이상 놓을 수 있는지?
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

min_length = 1
max_length = arr[-1] - arr[0]
result = 0
while min_length <= max_length:
    mid = (min_length + max_length) // 2

    cur = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] - cur >= mid:
            count += 1
            cur = arr[i]
    
    if count >= c:
        result = mid
        min_length = mid + 1
    else:
        max_length = mid - 1

print(result)