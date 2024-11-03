import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

# n 도시 / m 간선 / k 목표 거리 / x 시작 도시
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [INF] * (n+1)

distance[x] = 0

def bfs(x):
    q = deque()
    q.append(x)
    
    while q:
        city = q.popleft()
        dist = distance[city] + 1 
        
        for i in graph[city]:
            distance[i] = min(distance[i], dist)
            q.append(i)

bfs(x)

is_k = False
for i in range(1, n+1):
    if distance[i] == k:
        is_k = True
        print(i)

if not is_k:
    print(-1)
