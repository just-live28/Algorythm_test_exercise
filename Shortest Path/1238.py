import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(st):
    distance = [INF] * (n+1)
    distance[st] = 0
    
    q = []
    heapq.heappush(q, (0, st))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance

total_dist = [0] * (n+1)
return_distance = dijkstra(x)
for i in range(1, n+1):
    if i == x:
        continue
    distance = dijkstra(i)
    total_dist[i] += distance[x] + return_distance[i]

print(max(total_dist[1:]))