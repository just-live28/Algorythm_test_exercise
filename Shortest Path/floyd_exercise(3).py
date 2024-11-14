INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    start, end, dist = map(int, input().split())
    
    graph[start][end] = dist

for c in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cost = graph[a][c] + graph[c][b]
            if cost < graph[a][b]:
                graph[a][b] = cost

for a in range(1, n+1):
    for b in range(1, n+1):
        print(graph[a][b], end=' ')
    print()