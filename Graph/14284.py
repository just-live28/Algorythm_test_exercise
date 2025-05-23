import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
s, t = map(int, input().split())

distance = [INF] * (n+1)
distance[s] = 0

q = []
heapq.heappush(q, (0, s))
while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(distance[t])