from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n+1)
dist[x] = 0
q = deque()
q.append(x)
while q:
    now = q.popleft()
    
    for i in graph[now]:
        if dist[i] == -1:
            dist[i] = dist[now] + 1
            q.append(i)

result = []
for i in range(1, n+1):
    if dist[i] == k:
        result.append(i)
if not result:
    print(-1)
else:
    for i in result:
        print(i)