n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = arr[-1]

result = 0
while left <= right:
    mid = (left + right) // 2
    
    cur = 0
    for i in arr:
        if i - mid > 0:
            cur += i - mid
    
    if cur >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)