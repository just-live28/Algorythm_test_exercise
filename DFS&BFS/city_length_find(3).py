# n 도시 수 / m 도로 수 / k 목표 거리 / x 시작 도시
import heapq
INF = int(1e9)

n, m, k, x = map(int, input().split())

distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, dest = map(int, input().split())
    graph[start].append((dest, 1))

def dijkstra(start):
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, start = heapq.heappop(q)
        
        if dist > distance[start]:
            continue
        
        for i in graph[start]:
            cost = distance[start] + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.append((cost, i[0]))

dijkstra(x)

result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)