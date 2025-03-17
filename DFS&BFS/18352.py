from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append((x, 0))
distance[x] = 0
while q:
    now, dist = q.popleft()
    if dist > distance[now]:
        continue
    
    for i in graph[now]:
        if dist + 1 < distance[i]:
            distance[i] = dist + 1
            q.append((i, dist + 1))

result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)
if not result:
    print(-1)
else:
    for i in result:
        print(i)