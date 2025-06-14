from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
visited = [False] * (n+1)
visited[1] = True

count = 0
while q:
    now = q.popleft()

    for nxt in graph[now]:
        if not visited[nxt]:
            count += 1
            visited[nxt] = True
            q.append(nxt)

print(count)