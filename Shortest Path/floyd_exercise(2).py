import sys
input = sys.stdin.readline
INF = int(1e9)

v = int(input())
e = int(input())

graph = [[INF] * (v+1) for _ in range(v+1)]

for a in range(1, v+1):
    for b in range(1, v+1):
        if a == b:
            graph[a][b] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
for a in range(1, v+1):
    for b in range(1, v+1):
        for c in range(1, v+1):
            cost = graph[a][c] + graph[c][b]
            
            if cost < graph[a][b]:
                graph[a][b] = cost

for a in range(1, v+1):
    for b in range(1, v+1):
        print(graph[a][b], end=' ')
    print()
    