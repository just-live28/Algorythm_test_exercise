import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
st = int(input())
distance = [INF] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    # (en, d)
    graph[a].append((b, c))

def dijkstra(st):
    q = []
    heapq.heappush(q, (0, st))
    distance[st] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for nxt, val in graph[now]:
            cost = dist + val
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))

dijkstra(st)
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])