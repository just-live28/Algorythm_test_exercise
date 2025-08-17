n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
total_sum = arr[0]
en = 0
for st in range(n):
    while en < n and total_sum < m:
        en += 1
        if en < n:
            total_sum += arr[en]
    
    if en == n:
        break
    
    if total_sum == m:
        result += 1
    total_sum -= arr[st]

print(result)