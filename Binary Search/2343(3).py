n, m = map(int, input().split())
arr = list(map(int, input().split()))

min_time = max(arr)
max_time = sum(arr)
result = 0
while (min_time <= max_time):
    mid = (min_time + max_time) // 2

    count = 1
    cur = 0
    for disk in arr:
        if cur + disk > mid:
            count += 1
            cur = disk
        else:
            cur += disk

    if count <= m:
        result = mid
        max_time = mid - 1
    else:
        min_time = mid + 1

print(result)