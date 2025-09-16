# 도시 N(1~N번) / 도로 M(단방향) / 면접장 수 K
# 면접거리: 도달 가능 면접장 중 최소 거리 -> 면접 거리가 가장 긴 사람 및 거리 구하기
# 반대로 연결하고, 면접장으로부터 가장 먼 거리를 구하면 안되나? good
# 그리고 여러 면접장을 모두 시작점으로 해서 dijkstra를 수행한 뒤, 최대 거리와 그 도시 구하기

import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

def dijkstra(cities):
    distance = [INF] * (n+1)
    
    q = []
    for city in cities:
        heapq.heappush(q, (0, city))
        distance[city] = 0
    
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

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))

cities = list(map(int, input().split()))
min_distance = dijkstra(cities)

max_length = -1
max_idx = 0
for i in range(1, n+1):
    if min_distance[i] == INF:
        continue
    
    if min_distance[i] > max_length:
        max_length = min_distance[i]
        max_idx = i

print(max_idx)
print(max_length)