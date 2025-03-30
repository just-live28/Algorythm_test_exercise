n = 8
start_node = 1
graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
        ]

def dfs(node):
    # 현재 노드 방문 처리
    visited[node] = True
    print(node, end=' ')
    # 현재 노드의 인접 노드를 재귀적으로 방문
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

visited = [False] * (n+1)
dfs(start_node)     # 출력 : 1 2 7 6 8 3 4 5


# from collections import deque

# def bfs(graph, start_node, visited):
#     q = deque()
#     q.append(start_node)
#     visited[start_node] = True
    
#     while q:
#         now = q.popleft()
#         print(now, end=' ')
        
#         for i in graph[now]:
#             if not visited[i]:
#                 visited[i] = True
#                 q.append(i)

# visited = [False] * (n+1)
# bfs(graph, start_node, visited)     # 출력 : 1 2 3 8 7 4 5 6