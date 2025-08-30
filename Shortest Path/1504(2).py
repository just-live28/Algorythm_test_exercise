import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for nxt, length in graph[now]:
            cost = dist + length
            
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    
    return distance

length_v1_to_v2 = 0
length_v2_to_v1 = 0

distance_from_1 = dijkstra(1)
length_v1_to_v2 += distance_from_1[v1]
length_v2_to_v1 += distance_from_1[v2]
    
distance_from_v1 = dijkstra(v1)
length_v1_to_v2 += distance_from_v1[v2]
length_v2_to_v1 += distance_from_v1[n]

distance_from_v2 = dijkstra(v2)
length_v2_to_v1 += distance_from_v2[v1]
length_v1_to_v2 += distance_from_v2[n]

if length_v1_to_v2 >= INF and length_v2_to_v1 >= INF:
    print(-1)
else:
    print(min(length_v1_to_v2, length_v2_to_v1))