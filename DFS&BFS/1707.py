import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(node, color):
    global is_biperate
    visited[node] = color
    
    if not is_biperate:
        return
    
    for i in graph[node]:
        if visited[i] == color:
            is_biperate = False
            return
        if visited[i] == -1:
            if color == 1:
                dfs(i, 2)
            else:
                dfs(i, 1)

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [-1] * (v+1)
    is_biperate = True
    for i in range(1, v+1):
        if visited[i] == -1:
            dfs(i, 1)

    if is_biperate:
        print('YES')
    else:
        print('NO')