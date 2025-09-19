def split_snacks(arr, target):
    count = 0
    for i in arr:
        count += i // target
    
    return count

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

min_length = 1
max_length = max(snacks)
result = 0
while min_length <= max_length:
    mid = (min_length + max_length) // 2
    
    cur_snacks = split_snacks(snacks, mid)
    if cur_snacks >= m:
        result = mid
        min_length = mid + 1
    else:
        max_length = mid - 1

print(result)