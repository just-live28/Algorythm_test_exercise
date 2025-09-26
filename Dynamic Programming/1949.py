# d[i][0] : i번 마을이 일반마을일 때, 서브트리의 최대 우수마을 주민 수
# d[i][1] : i번 마을이 우수마을일 때, 서브트리의 최대 우수마을 주민 수
import sys
sys.setrecursionlimit(10 ** 5)

def dfs(now, parent):
    d[now][0] = 0
    d[now][1] = arr[now]
    
    for nxt in graph[now]:
        if nxt == parent:
            continue
        
        dfs(nxt, now)
        
        d[now][0] += max(d[nxt][0], d[nxt][1])
        d[now][1] += d[nxt][0]

n = int(input())
arr = [None] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

d = [[0] * 2 for _ in range(n+1)]
dfs(1, 0)

print(max(d[1][0], d[1][1]))