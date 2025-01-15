import heapq
INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (N+1)

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
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

max_length = 0
enable_city = 0
for i in range(1, N+1):
    if distance[i] != INF:
        enable_city += 1
        max_length = max(max_length, distance[i])

print(enable_city-1, max_length)