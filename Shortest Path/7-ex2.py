INF = int(1e9)

n = int(input())
m = int(input())

d = [[INF] * (n+1) for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, n+1):
        if x == y:
            d[x][y] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    d[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            d[a][b] = min(d[a][b], d[a][k] + d[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if d[i][j] == INF:
            print('INFINITY', end=' ')
        else:
            print(d[i][j], end=' ')
    print()