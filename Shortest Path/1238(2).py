import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    distance = [INF] * (n+1)
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
        
    return distance

total_length = [0] * (n+1)
for i in range(1, n+1):
    if i == x:
        continue
    
    start_distance = dijkstra(i)
    total_length[i] += start_distance[x]

dest_distance = dijkstra(x)
for i in range(1, n+1):
    if i == x:
        continue
    total_length[i] += dest_distance[i]

print(max(total_length[1:]))