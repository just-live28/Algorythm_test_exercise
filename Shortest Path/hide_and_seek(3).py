# 양방향 통로
# 1번에서 출발
# 최단 거리 헛간
import heapq
import sys
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

spaces = []
max_value = 0
max_idx = 0
for i in range(1, n+1):
    if distance[i] > max_value:
        spaces.clear()
        
        max_value = distance[i]
        max_idx = i
        spaces.append(distance[i])
    elif distance[i] == max_value:
        spaces.append(distance[i])

print(max_idx, max_value, len(spaces))
        
    
    
