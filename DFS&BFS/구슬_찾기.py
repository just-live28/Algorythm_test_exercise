INF = int(1e9)

n, m = map(int, input().split())
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dist[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            cost = dist[i][k] + dist[k][j]
            if cost < dist[i][j]:
                dist[i][j] = cost

result = 0
for i in range(1, n+1):
    light = 0
    heavy = 0
    for j in range(1, n+1):
        if i == j:
            continue
        if dist[i][j] != INF:
            light += 1
        if dist[j][i] != INF:
            heavy += 1
    half = (n-1) // 2
    if light > half or heavy > half:
        result += 1
        
print(result)