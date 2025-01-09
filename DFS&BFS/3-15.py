from collections import deque
INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)] 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [INF] * (n+1)

q = deque()
q.append((x, 0))
distance[x] = 0

while q:
    now, dist = q.popleft()
    
    if dist > distance[now]:
        continue
    
    for i in graph[now]:
        cost = distance[now] + 1
        if cost < distance[i]:
            distance[i] = cost
            q.append((i, cost))

result = []
for i in range(1, len(distance)):
    if distance[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)