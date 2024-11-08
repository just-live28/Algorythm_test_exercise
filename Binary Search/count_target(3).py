from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

arr = list(map(int, input().split()))

left = bisect_left(arr, x)
right = bisect_right(arr, x)

result = right - left

if result == 0:
    print(-1)
else:
    print(result)