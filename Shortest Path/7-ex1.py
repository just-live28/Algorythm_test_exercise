import heapq
INF = int(1e9)

# n 노드 개수 / m 간선 개수
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    
    # 시작노드 -> (끝노드, 거리)
    graph[a].append((b, c))

distance = [INF] * (n+1)

def dijkstra(start):
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        # i[0] 도착노드 i[1] 거리
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])