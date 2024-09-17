import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

# n 학생 수 m 비교 수
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

# (더높은사람, 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    reverse_graph[b].append((a,1))


def dijkstra(start):
    distance = [INF] * (n+1)
    reverse_distance = [INF] * (n+1)
    distance[start] = reverse_distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, loc = heapq.heappop(q)
        if dist > distance[loc]:
            continue
        for i in graph[loc]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    q2 = []
    heapq.heappush(q2, (0, start))
    while q2:
        dist, loc = heapq.heappop(q2)
        if dist > reverse_distance[loc]:
            continue
        for i in reverse_graph[loc]:
            cost = dist + i[1]
            if cost < reverse_distance[i[0]]:
                reverse_distance[i[0]] = cost
                heapq.heappush(q2, (cost, i[0]))

    is_correct = True
    for i in range(1, n+1):
        if distance[i] == INF and reverse_distance[i] == INF:
            is_correct = False
    return is_correct

total = 0
for i in range(1, n+1):
    if dijkstra(i):
        total += 1
print(total)