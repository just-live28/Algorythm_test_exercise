INF = int(1e9)

N, M = map(int, input().split())
dist = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            dist[i][j] = 0

for _ in range(M):
    A, B = map(int, input().split())
    dist[A][B] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

total_count = 0
for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if dist[i][j] != INF or dist[j][i] != INF:
            count += 1
    if count == N:
        total_count += 1

print(total_count)