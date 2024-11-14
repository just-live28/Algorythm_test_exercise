import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, n+1):
        if x == y:
            graph[x][y] = 0
            
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

row = [0] * (n+1)
column = [0] * (n+1)
for a in range(1, n+1):
    for b in range(1, n+1):
        if 0 < graph[a][b] < INF:
            row[a] += 1
            column[b] += 1

count = 0
for i in range(1, n+1):
    if row[i] + column[i] == n-1:
        count += 1

print(count)