from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()

def bfs(v):
    visited = [False] * (n+1)
    q = deque()
    q.append(v)
    visited[v] = True
    result = [v]
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                result.append(i)
                q.append(i)
    return result

dfs_visited = [False] * (n+1)
dfs_result = [v]
def dfs(v):
    dfs_visited[v] = True
    
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs_result.append(i)
            dfs(i)

dfs(v)
print(*dfs_result)
print(*bfs(v))