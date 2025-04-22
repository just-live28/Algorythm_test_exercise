n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

def dfs(x):
    visited[x] = True
    
    for nxt in graph[x]:
        if not visited[nxt]:
            dfs(nxt)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)
        
print(count)