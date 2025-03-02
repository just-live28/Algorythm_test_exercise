import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
pre = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

def dijkstra(start):
    distance[start] = 0
    pre[start] = 0
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
                pre[i[0]] = now
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[end])
count = 1
cur = end
result = [end]
while pre[cur] != 0:
    cur = pre[cur]
    count += 1
    result.append(cur)
result.reverse()
print(count)
print(*result)