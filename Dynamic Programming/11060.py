INF = int(1e9)

n = int(input())
arr = [0] + list(map(int, input().split()))

d = [INF] * (n+1)
d[1] = 0

for i in range(1, n+1):
    enable = arr[i]
    for j in range(1, enable + 1):
        if i+j <= n:
            d[i+j] = min(d[i+j], d[i] + 1)

result = d[n]
if result == INF:
    print(-1)
else:
    print(result)