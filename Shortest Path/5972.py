import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [INF] * (n+1)
distance[1] = 0
q = []
heapq.heappush(q, (0, 1))
while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(distance[n])