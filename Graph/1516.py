from collections import deque

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
times = [0] * (n+1)
result = [0] * (n+1)

for i in range(1, n+1):
    line = list(map(int, input().split()))[:-1]
    times[i] = line[0]
    result[i] = line[0]
    
    for j in line[1:]:
        indegree[i] += 1
        graph[j].append(i)

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

visited = [False] * (n+1)
while q:
    now = q.popleft()
    visited[now] = True
    
    for nxt in graph[now]:
        indegree[nxt] -= 1
        result[nxt] = max(result[nxt], result[now] + times[nxt])
        if indegree[nxt] == 0:
            q.append(nxt)

for i in result[1:]:
    print(i)