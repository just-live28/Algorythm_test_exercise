import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v, color):
    global is_biparite
    visited[v] = color
    
    if not is_biparite:
        return
    
    for i in graph[v]:
        if visited[i] == color:
            is_biparite = False
            return
        elif visited[i] == 0:
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

    is_biparite = True
    visited = [0] * (v+1)

    for i in range(1, v+1):
        if visited[i] == 0:
            dfs(i, 1)
    if is_biparite:
        print("YES")
    else:
        print("NO")