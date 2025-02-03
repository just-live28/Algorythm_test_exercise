from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(start):
    q = deque()
    q.append(start)
    
    visited = [-1] * (n+1)
    visited[start] = 0
    
    while q:
        now = q.popleft()
        
        for node, weight in graph[now]:
            if visited[node] == -1:
                visited[node] = visited[now] + weight
                q.append(node)
    # 최대 경로를 이루는 노드, 최대 경로 합 반환
    return visited.index(max(visited)), max(visited)

# node1, _ = bfs(1)
# node2, diameter = bfs(node1)
# print(diameter)
# 위의 세 줄을 한 줄로 표현하면 아래와 같다.
print(bfs(bfs(1)[0])[1])