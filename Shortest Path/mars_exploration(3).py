INF = int(1e9)
from collections import deque

tc = int(input())

results = []
for _ in range(tc):
    n = int(input())

    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    d = [[INF]*n for _ in range(n)]
    d[0][0] = graph[0][0]

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
                
            if 0 <= nx < n and 0 <= ny < n:
                cost = d[x][y] + graph[nx][ny]
                
                if cost < d[nx][ny]:
                    d[nx][ny] = cost
                    q.append((nx, ny))

    results.append(d[n-1][n-1])

for result in results:
    print(result)