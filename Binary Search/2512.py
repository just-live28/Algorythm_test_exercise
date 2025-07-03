n = int(input())
arr = list(map(int, input().split()))
money = int(input())

left = 1
right = max(arr)
result = 0
while left <= right:
    mid = (left + right) // 2

    total = 0
    for i in arr:
        if i > mid:
            total += mid
        else:
            total += i
    
    if total <= money:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)