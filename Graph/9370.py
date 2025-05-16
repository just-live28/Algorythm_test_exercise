import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

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

tc = int(input())
for _ in range(tc):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    distance_s = dijkstra(s)
    distance_g = dijkstra(g)
    distance_h = dijkstra(h)
    
    result = []
    for _ in range(t):
        x = int(input())
        
        if distance_s[g] + distance_g[h] + distance_h[x] == distance_s[x] or distance_s[h] + distance_h[g] + distance_g[x] == distance_s[x]:
            result.append(x)
    result.sort()
    print(*result)