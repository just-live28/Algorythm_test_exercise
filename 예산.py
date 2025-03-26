n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr.sort()

def is_enable(limit):
    remain = m
    for i in range(n):
        if arr[i] <= limit:
            remain -= arr[i]
        else:
            remain -= limit
    if remain < 0:
        return False
    return True

left = 0
right = arr[-1]
result = 0
while left <= right:
    mid = (left + right) // 2
    
    if is_enable(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)