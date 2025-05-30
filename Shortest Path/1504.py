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

dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

result1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]
result2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]

if result1 >= INF and result2 >= INF:
    print(-1)
else:
    print(min(result1, result2))