from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())    
    graph[a].append(b)
    graph[b].append(a)
    
q = deque()
q.append(1)

visited = [False] * (v+1)
visited[1] = True

count = 0
while q:
    now = q.popleft()
    
    for i in graph[now]:
        if visited[i] == False:
            visited[i] = True
            count += 1
            q.append(i)

print(count)