import heapq
INF = int(1e9)

# n 회사 m 경로
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

# a 시작 b 도착 c 거리
for _ in range(m):
    a, b = map(int ,input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

def dijkstra(start, target):
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
                q.append((cost, i[0]))
    
    return distance[target]


result = dijkstra(1, k) + dijkstra(k, x)

if result >= INF:
    print(-1)
else:
    print(result)