import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

# b 도착도시 c 비용
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    # (비용, 도착도시)
    heapq.heappush(q, (0, start))
    while q:
        dist, loc = heapq.heappop(q)
        if dist > distance[loc]:
            continue
        for i in graph[loc]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    for i in range(1,n+1):
        if distance[i] == INF:
            print(0, end=' ')
        else:
            print(distance[i], end=' ')
    print()

for i in range(1, n+1):
    dijkstra(i)