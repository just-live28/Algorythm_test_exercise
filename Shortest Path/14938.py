import heapq
INF = int(1e9)

n, m, r = map(int, input().split())
arr = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance

max_count = 0
for st in range(1, n+1):
    distance = dijkstra(st)

    count = arr[st]
    for en in range(1, n+1):
        if en == st:
            continue

        if distance[en] <= m:
            count += arr[en]
    
    max_count = max(max_count, count)

print(max_count)