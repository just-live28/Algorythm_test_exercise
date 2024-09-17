import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # (도착지, 비용)
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (n+1)
distance[1] = 0
q = []
heapq.heappush(q, (0, 1))

max_index = 0
max_length = 0
while q:
    dist, loc = heapq.heappop(q)
    if dist > distance[loc]:
        continue
    for i in graph[loc]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
            if cost > max_length:
                max_index = i[0]
                max_length = cost

same_length_count = 0
for i in distance:
    if i == max_length:
        same_length_count += 1

print(max_index,max_length,same_length_count)