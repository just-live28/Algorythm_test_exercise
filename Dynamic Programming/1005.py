import sys
input = sys.stdin.readline

def go(now):
    if d[now] != -1:
        return d[now]
    
    d[now] = 0
    for nxt in graph[now]:
        d[now] = max(d[now], go(nxt))
    
    d[now] = d[now] + times[now]
    return d[now]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    times = [None] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y].append(x)

    d = [-1] * (n+1)
    w = int(input())

    print(go(w))