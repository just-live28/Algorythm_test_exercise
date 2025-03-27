import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
info = input().rstrip()
arr = [0]
for i in info:
    arr.append(int(i))

graph = [[] for _ in range(n+1)]
count = 0
visited = [False] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    if arr[a] == 1 and arr[b] == 1:
        count += 2

def outdoor_dfs(v):
    visited[v] = True
    
    inside_count = 0
    for u in graph[v]:
        if not visited[u] and arr[u] == 0:
            inside_count += outdoor_dfs(u)
        elif arr[u] == 1:
            inside_count += 1
    return inside_count

for i in range(1, n+1):
    if not visited[i] and arr[i] == 0:
        inside_count = outdoor_dfs(i)
        count += inside_count * (inside_count - 1)

print(count)