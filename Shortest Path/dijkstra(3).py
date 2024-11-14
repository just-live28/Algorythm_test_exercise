import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e, s = map(int, input().split())

graph = [[] for _ in range(v+1)]

# graph[시작] = (끝, 거리)
for _ in range(e):
    start, end, length = map(int, input().split())
    graph[start].append((end, length))

distance = [INF] * (v+1)
distance[s] = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, depart = heapq.heappop(q)
        
        if dist > distance[depart]:
            continue
        
        for i in graph[depart]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(s)
print(distance)
            

