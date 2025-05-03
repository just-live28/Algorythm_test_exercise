from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    delays = [0] + list(map(int, input().split()))
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        indegree[y] += 1
        graph[x].append(y)
    w = int(input())

    d = [0] * (n+1)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            d[i] = delays[i]
            q.append(i)
    
    while q:
        now = q.popleft()
        
        for nxt in graph[now]:
            d[nxt] = max(d[nxt], d[now] + delays[nxt])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    print(d[w])