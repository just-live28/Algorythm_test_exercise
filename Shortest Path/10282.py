import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

tc = int(input())
for _ in range(tc):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    distance = [INF] * (n+1)
    distance[c] = 0

    q = []
    heapq.heappush(q, (0, c))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    max_time = 0
    count = 0
    for time in distance[1:]:
        if time == INF:
            continue

        count += 1
        max_time = max(max_time, time)

    print(count, max_time)