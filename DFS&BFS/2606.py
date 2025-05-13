from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
visited[1] = True
q = deque()
q.append(1)
result = 0
while q:
    now = q.popleft()
    
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)
            result += 1

print(result)    