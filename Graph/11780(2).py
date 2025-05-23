import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]
nxt = [[-1] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c
        nxt[a][b] = b

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or dist[i][j] == INF:
            print(0)
        else:            
            result = []
            cur = i
            while cur != j:
                result.append(cur)
                cur = nxt[cur][j]
            result.append(j)
            print(len(result), end=' ')
            print(*result)