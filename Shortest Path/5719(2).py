import sys
import heapq
from collections import deque
INF = int(1e9)
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    st, en = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))

    q = []
    heapq.heappush(q, (0, st))
    distance = [INF] * (n+1)
    distance[st] = 0
    routes = [[] for _ in range(n+1)]
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                routes[i[0]].clear()
                routes[i[0]].append(now)
            elif cost == distance[i[0]]:
                routes[i[0]].append(now)

    rq = deque()
    visited = set()
    ban_routes = set()
    for i in routes[en]:
        rq.append((i, en))
        visited.add((i, en))

    while rq:
        start, end = rq.popleft()
        ban_routes.add((start, end))

        for i in routes[start]:
            if (i, start) not in visited:
                rq.append((i, start))
                visited.add((i, start))

    distance = [INF] * (n+1)
    distance[st] = 0
    q = []
    heapq.heappush(q, (0, st))
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            if (now, i[0]) in ban_routes:
                continue

            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    if distance[en] == INF:
        print(-1)
    else:
        print(distance[en])