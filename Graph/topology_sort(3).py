from collections import deque

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())

    graph[a].append(b)
    indegree[b] += 1

q = deque()

for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in result:
    print(i, end=' ')

