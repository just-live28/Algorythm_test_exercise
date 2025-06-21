INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = INF
for i in range(1, v+1):
    for j in range(1, v+1):
        if i == j:
            result = min(result, graph[i][i])
        else:
            result = min(result, graph[i][j] + graph[j][i])

if result == INF:
    print(-1)
else:
    print(result)