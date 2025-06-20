import heapq
INF = int(1e9)

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    srt, dst = map(int, input().split())
    graph[srt].append((dst, 1))
    graph[dst].append((srt, 1))

distance = [INF] * (n+1)
distance[a] = 0
q = []
heapq.heappush(q, (0, a))
while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

if distance[b] == INF:
    print(-1)
else:
    print(distance[b])