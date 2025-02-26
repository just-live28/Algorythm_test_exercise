# 무방향 그래프, 연결 요소 개수(덩어리) 구하기
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS
# visited = [False] * (n+1)
# count = 0
# q = deque()
# for i in range(1, n+1):
#     if not visited[i]:
#         count += 1
#         visited[i] = True
#         q.append(i)
#         while q:
#             now = q.popleft()
#             for j in graph[now]:
#                 if not visited[j]:
#                     visited[j] = True
#                     q.append(j)
# print(count)

# 비재귀 DFS (정석 DFS식)
stack = []
visited = [False] * (n+1)
count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        stack.append(i)
        
        while stack:
            now = stack.pop()
            if visited[now]:
                continue
            visited[now] = True
            for j in graph[now]:
                stack.append(j)
    
print(count)