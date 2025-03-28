import sys
import heapq
INF = int(1e9)
sys.setrecursionlimit(10**5)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
path = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    # (도착도시, 시간)
    graph[a].append((b, c))
start, end = map(int, input().split())

distance = [-INF] * (n+1)
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        dist *= (-1)
        
        if dist < distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost > distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (-cost, i[0]))
                path[i[0]].clear()
                path[i[0]].append(now)
            elif cost == distance[i[0]]:
                path[i[0]].append(now)

visited = set()
def count_road(city):
    global road
    if city == start:
        return
    for i in path[city]:
        if (city, i) not in visited:
            visited.add((city, i))
            road += 1
            count_road(i)

dijkstra(start)
road = 0
count_road(end)

print(distance[end])
print(road)