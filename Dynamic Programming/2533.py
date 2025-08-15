import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

d = [[0] * 2 for _ in range(n+1)]
for i in range(1, n+1):
    d[i][1] = 1

def dfs(x, p):
    for child in graph[x]:
        if child == p:
            continue
        dfs(child, x)
        d[x][0] += d[child][1]
        d[x][1] += min(d[child][0], d[child][1])

dfs(1, 0)
print(min(d[1][0], d[1][1]))