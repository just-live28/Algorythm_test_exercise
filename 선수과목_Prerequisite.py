from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

def topological_sort():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append((i, 1))
    
    result = [0] * (n+1)
    while q:
        now, term = q.popleft()
        result[now] = term
        
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append((nxt, term + 1))

    return result

print(*topological_sort()[1:])