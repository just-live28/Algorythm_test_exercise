# n개의 도시 (단방향 연결)
# c에서 전보를 뿌린다.
# 전보를 받는 총 도시(비용이 INF가 아닌 도시의 개수)
# 전보를 모두 받는데까지 걸리는 시간(INF가 아닌 비용 중 가장 큰 비용)
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

# 도시n 통로m 시작도시c
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    # (도착지, 비용)
    graph[a].append((b, cost))

distance = [INF] * (n+1)

def dijkstra(start):
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

dijkstra(c)

count = 0
max_time = 0
for i in range(1, n+1):
    if i != c and distance[i] != INF:
        count += 1
        if distance[i] > max_time:
            max_time = distance[i]

print(count, max_time)