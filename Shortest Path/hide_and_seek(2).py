import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (n+1)

distance[1] = 0

q = []
heapq.heappush(q, (0, 1))

while q:
    dist, now = heapq.heappop(q)
    
    if dist > distance[now]:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]
        
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

max_idx = -1
max_length = 0
count = 0
for i in range(1, n+1):
    if distance[i] > max_length:
        max_idx = i
        max_length = distance[i]
        
        count = 1
        continue
    
    if distance[i] == max_length:
        count += 1

print(max_idx, max_length, count)