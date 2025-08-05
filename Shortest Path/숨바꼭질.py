# N개의 헛간(1~N) / 1번 시작 / M개의 양방향 통로(항상 도달 가능)
# 가장 안전(최단 거리가 가장 먼 헛간)
# 헛간 번호(거리 중복 시 가장 작은 번호) / 거리 / 같은 헛간 개수

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

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

min_idx = 0
max_length = -1
count = 0
for i in range(1, n+1):
    dist = distance[i]

    if dist > max_length:
        count = 1
        max_length = dist
        min_idx = i
    elif dist == max_length:
        count += 1

print(min_idx, max_length, count)