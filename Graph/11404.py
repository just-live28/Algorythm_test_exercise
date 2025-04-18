# 단방향
# 시작 도시 도착 도시를 연결하는 노선은 하나가 아닐 수 있다

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dist[i][j] = 0
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] >= INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()