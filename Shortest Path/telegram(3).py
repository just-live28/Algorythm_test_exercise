import heapq
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

# x 시작 y 도착지 z 거리
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
distance = [INF] * (n+1)

def dijkstra(start):
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.append((cost, i[0]))

dijkstra(c)

enable_city = 0
max_length = 0
for i in range(1, n+1):
    if i == c:
        continue
    
    if distance[i] != INF:
        enable_city += 1
        max_length = max(max_length, distance[i])

print(distance)
print(enable_city, end=' ')
print(max_length)
