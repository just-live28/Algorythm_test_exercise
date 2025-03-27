n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

visited = [False] * (n+1)
count = 0
for v in range(1, n+1):
    if not visited[v]:
        count += 1
        dfs(v)

print(count)