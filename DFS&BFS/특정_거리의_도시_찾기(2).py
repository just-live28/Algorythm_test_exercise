# 1~N까지의 도시 / M 도로(단방향) - 거리 1
# X로부터 출발하여 도달할 수 있는 도시 중, 최단 거리가 정확히 K인 모든 도시 출력하기
# 거리가 1이므로, 먼저 도달만 하면 최초 방문 도시. visited를 이제 t/f가 아니라, 현재 count로 INF만 아니게끔 바꾸기
# 큐에 (0, X)를 넣고 시작, pop => (count, now)한 후, graph[now]에 대해서, visited[nxt] 가 INF라면 count로 바꾼 후, (count + 1, nxt)를 큐에 추가
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [INF] * (n+1)
distance[x] = 0
q = deque()
q.append((0, x))
while q:
    count, now = q.popleft()
    
    for nxt in graph[now]:
        if distance[nxt] == INF:
            distance[nxt] = count + 1
            q.append((count + 1, nxt))

result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

if not result:
    print(-1)
else:
    for city in result:
        print(city)