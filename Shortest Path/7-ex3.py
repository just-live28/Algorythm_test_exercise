INF = int(1e9)

n, m = map(int, input().split())

d = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    d[start][end] = 1
    d[end][start] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            d[i][j] = 0

for c in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            d[a][b] = min(d[a][b], d[a][c] + d[c][b])

x, k = map(int, input().split())
distance = d[1][k] + d[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)