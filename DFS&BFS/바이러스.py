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
count = 0
while q:
    now = q.popleft()
    
    for i in graph[now]:
        if not visited[i]:
            count += 1
            visited[i] = True
            q.append(i)

print(count)