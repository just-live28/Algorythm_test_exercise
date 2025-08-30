import heapq
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    st, en, t = map(int, input().split())
    graph[st].append((en, t))

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

go_home_distance = dijkstra(x)
result = [0] * (n+1)
for j in range(1, n+1):
    if j == x:
        continue
    
    go_party_distance = dijkstra(j)
    result[j] = go_party_distance[x] + go_home_distance[j]

print(max(result))