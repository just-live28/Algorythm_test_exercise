from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs_visited = [False] * (n+1)
dfs_visited[v] = True

dfs_result = []
def dfs(node):
    dfs_result.append(node)
    
    for i in graph[node]:
        if dfs_visited[i] == False:
            dfs_visited[i] = True
            dfs(i)

dfs(v)

def bfs(start):
    bfs_visited = [False] * (n+1)
    bfs_visited[start] = True
    
    q = deque()
    q.append(start)
    
    bfs_result = []
    while q:
        now = q.popleft()
        bfs_result.append(now)
        
        for i in graph[now]:
            if bfs_visited[i] == False:
                bfs_visited[i] = True
                q.append(i)

    return bfs_result
        
bfs_result = bfs(v)

for i in dfs_result:
    print(i, end=' ')
print()
for i in bfs_result:
    print(i, end=' ')