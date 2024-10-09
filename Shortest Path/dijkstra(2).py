import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

start = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    # (도착지, 비용)
    graph[a].append((b, c))

distance = [INF] * (v+1)

def dijkstra(start):
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, city  = heapq.heappop(q)
        
        if dist > distance[city]:
            continue
        
        for i in graph[city]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, v+1):
    print(distance[i])