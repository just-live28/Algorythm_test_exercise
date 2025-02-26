# 양방향 연결
# 방문 정점이 여러개인 경우 번호가 작은 것을 먼저 방문

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

def bfs(start):
    bfs_visited = [False] * (n+1)
    q = deque()
    q.append(start)
    bfs_visited[start] = True
    
    result = [start]
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if not bfs_visited[i]:
                bfs_visited[i] = True
                result.append(i)
                q.append(i)
    
    print(*result)
    
def dfs(node):
    if dfs_visited[node]:
        return
    dfs_visited[node] = True
    dfs_result.append(node)
    for i in graph[node]:
        dfs(i)
                
dfs_visited = [False] * (n+1)
dfs_result = []
dfs(v)
print(*dfs_result)
bfs(v)