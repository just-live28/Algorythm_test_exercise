from collections import deque
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

while True:
    n, m = map(int, input().split())

    if (n, m) == (0, 0):
        break

    start, dest = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))

    distance = [INF] * n
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    routes = [[] for _ in range(n)]
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                routes[i[0]] = [now]
            elif cost == distance[i[0]]:
                routes[i[0]].append(now)

    # routes로부터 dest ~ start 의 경로들을 set에 추가
    ban_routes = set()
    rq = deque()
    visited = set()
    for i in routes[dest]:
        rq.append((dest, i))
        visited.add((dest, i))
    while rq:
        route_dst, route_st = rq.popleft()
        ban_routes.add((route_st, route_dst))

        for i in routes[route_st]:
            if (route_st, i) not in visited:
                rq.append((route_st, i))
                visited.add((route_st, i))

    distance = [INF] * n
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
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

    if distance[dest] == INF:
        print(-1)
    else:
        print(distance[dest])