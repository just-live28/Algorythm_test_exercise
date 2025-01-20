import heapq
INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (N+1)
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

max_index = 0
max_length = 0
count = 0
for i in range(2, N+1):
    if distance[i] > max_length:
        max_index = i
        max_length = distance[i]
        count = 1
    elif distance[i] == max_length:
        count += 1

print(max_index, max_length, count)