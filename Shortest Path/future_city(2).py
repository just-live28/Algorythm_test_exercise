# 1~N 까지의 회사 (도로 간 양방향 연결. 거리 1)
# 1번 도시에 위치, X번 회사에 방문해 물건 판매
# A -> K -> X
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            cost = graph[a][c] + graph[c][b]
            
            if cost < graph[a][b]:
                graph[a][b] = cost

dist = graph[1][k] + graph[k][x]
if dist >= INF:
    print(-1)
else:
    print(dist)