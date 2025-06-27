import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

distance = [INF] * (n+1)
distance[x] = 0
q = []
heapq.heappush(q, (0, x))

while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

if not result:
    print(-1)
else:
    for j in result:
        print(j)