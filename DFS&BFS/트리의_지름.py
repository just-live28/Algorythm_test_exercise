from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(node):
    result = [0] * (n+1)
    visited = [False] * (n+1)
    q = deque()
    q.append((node, 0))
    visited[node] = True
    
    while q:
        now, cost = q.popleft()
        
        complete = True
        for nxt, val in graph[now]:
            if not visited[nxt]:
                complete = False
                visited[nxt] = True
                q.append((nxt, cost + val))
        
        if complete:
            result[now] = cost
    
    return max(result), result.index(max(result))

print(bfs(bfs(1)[1])[0])