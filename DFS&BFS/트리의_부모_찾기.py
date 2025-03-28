from collections import deque

# 1부터 bfs를 돌며 자식들에게 부모를 세팅.
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * (n+1)
visited[1] = int(1e9)
q = deque()
q.append(1)

while q:
    now = q.popleft()
    
    for i in graph[now]:
        if visited[i] == -1:
            visited[i] = now
            q.append(i)

for i in visited[2:]:
    print(i)