from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    
    indegree[b] += 1
    graph[a].append(b)

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(now)
    
    for j in graph[now]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.append(j)

print(*result)        