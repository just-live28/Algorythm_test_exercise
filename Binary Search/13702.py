n, k = map(int, input().split())
arr = []
min_val = 1
max_val = 1000000
for _ in range(n):
    num = int(input())
    max_val = max(max_val, num)
    arr.append(num)

result = 0
while (min_val <= max_val):
    mid = (min_val + max_val) // 2

    count = 0
    for i in arr:
        count += i // mid
    
    if count >= k:
        result = mid
        min_val = mid + 1
    else:
        max_val = mid - 1

print(result)