INF = int(1e9)

n, m = map(int, input().split())

d = [[INF] * (n+1) for _ in range(n+1)]
reverse_d = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    d[i][i] = 0
    reverse_d[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    d[a][b] = 1
    reverse_d[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            reverse_d[i][j] = min(reverse_d[i][j], reverse_d[i][k] + reverse_d[k][j])

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if i == j:
            continue
        if d[i][j] != INF:
            count += 1
        if reverse_d[i][j] != INF:
            count += 1
    
    if count == n-1:
        result += 1

print(result)