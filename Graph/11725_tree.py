from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
parent = [0] * (n+1)
q = deque()
q.append(1)
while q:
    now = q.popleft()
    
    for i in graph[now]:
        if i == parent[now]:
            continue
        q.append(i)
        parent[i] = now

for i in parent[2:n+1]:
    print(i)