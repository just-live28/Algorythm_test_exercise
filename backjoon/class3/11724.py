from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

result = 0
for i in range(1, n+1):
    if visited[i] == False:
        visited[i] = True
        result += 1
        
        q = deque()
        q.append(i)
        
        while q:
            now = q.popleft()
            
            for j in graph[now]:
                if visited[j] == False:
                    visited[j] = True
                    q.append(j)

print(result)