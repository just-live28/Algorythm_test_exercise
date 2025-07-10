n, m = map(int, input().split())
arr = list(map(int, input().split()))
end = n - m

result = sum(arr[0:m])
cur = result
for i in range(m, n):
    cur += arr[i]
    cur -= arr[i-m]
    result = max(cur, result)

print(result)