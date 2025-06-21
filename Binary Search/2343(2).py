n, m = map(int, input().split())
arr = list(map(int, input().split()))

min_length = 0
for i in arr:
    min_length = max(min_length, i)
max_length = sum(arr)

result = 0
while min_length <= max_length:
    mid = (min_length + max_length) // 2

    count = 1
    cur = 0
    for i in arr:
        if cur + i <= mid:
            cur += i
        else:
            count += 1
            cur = i
    
    if count <= m:
        result = mid
        max_length = mid - 1
    else:
        min_length = mid + 1

print(result)