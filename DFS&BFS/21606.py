import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
nodes = [0]
for i in input().rstrip():
    nodes.append(int(i))
graph = [[] for _ in range(n+1)]
COUNT = 0
for _ in range(n-1):
    a, b = map(int, input().split())
    if nodes[a] == 1 and nodes[b] == 1:
        COUNT += 2
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True
    
    inside_count = 0
    for j in graph[node]:
        if nodes[j] == 0 and not visited[j]:
            inside_count += dfs(j)
        elif nodes[j] == 1:
            inside_count += 1

    return inside_count

visited = [False] * (n+1)
for i in range(1, n+1):
    if nodes[i] == 0 and not visited[i]:
        inside_count = dfs(i)
        COUNT += inside_count * (inside_count - 1)
        
print(COUNT)