from collections import deque
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    # (도착지, 비용)
    graph[a].append((b, c))
st, en = map(int, input().split())

distance = [INF] * (n+1)

def dijkstra(st):
    distance[st] = 0
    q = deque()
    q.append((0, st))
    
    while q:
        dist, now = q.popleft()
        
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.append((cost, i[0]))

dijkstra(st)
print(distance[en])