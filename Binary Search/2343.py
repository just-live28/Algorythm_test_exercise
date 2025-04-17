n, m = map(int, input().split())
arr = list(map(int, input().split()))

def count_blueray(arr, length):
    br_count = 0
    sum_time = 0
    for i in range(n):
        if sum_time + arr[i] <= length:
            sum_time += arr[i]
        else:
            br_count += 1
            sum_time = arr[i]
    if sum_time > 0:
        return br_count + 1
    return br_count

min_length = max(arr)
max_length = sum(arr)
result = 0
while (min_length <= max_length):
    
    mid = (min_length + max_length) // 2
    
    count = count_blueray(arr, mid)
    if count <= m:
        result = mid
        max_length = mid - 1
    else:
        min_length = mid + 1

print(result)