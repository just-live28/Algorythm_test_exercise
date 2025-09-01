import heapq
INF = int(1e9)

n, m = map(int, input().split())
st = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
heapq.heappush(q, (0, st))
distance = [INF] * (n+1)
distance[st] = 0
while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue
    
    for i in graph[now]:
        # i[0] : nxt / i[1]: c(now -> nxt)
        cost = dist + i[1]
        
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(distance[1:])