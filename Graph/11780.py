import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]
next = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dist[i][j] = 0
            next[i][j] = 0
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    next[a][b] = b

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            cost = dist[i][k] + dist[k][j]
            if cost < dist[i][j]:    
                dist[i][j] = cost
                next[i][j] = next[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] >= INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == 0 or dist[i][j] == INF:
            print(0)
            continue
        count = 1
        result = [i]
        cur = i
        while cur != j:
            cur = next[cur][j]
            count += 1
            result.append(cur)
        print(count, end=' ')
        print(*result)