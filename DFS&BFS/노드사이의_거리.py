from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def find_length(st, en):
    visited = [False] * (n+1)
    q = deque()
    q.append((st, 0))
    visited[st] = True
    
    while q:
        now, cost = q.popleft()
        
        if now == en:
            return cost
        
        for nxt in graph[now]:
            if not visited[nxt[0]]:
                visited[nxt[0]] = True
                q.append((nxt[0], nxt[1] + cost))

for _ in range(m):
    a, b = map(int, input().split())
    print(find_length(a, b))