import sys
input = sys.stdin.readline
from collections import deque

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for _ in range(n+1)]

    for i in range(n-1):
        for j in range(i+1, n):
            a, b = arr[i], arr[j]
            
            graph[a][b] = True
            indegree[b] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    is_impossible = False
    is_unknown = False
    while q:
        if len(q) > 1:
            is_unknown = True
            break
        
        now = q.popleft()
        result.append(now)
        
        for nxt in range(1, n+1):
            if nxt == now:
                continue
            
            if graph[now][nxt]:
                indegree[nxt] -= 1
                
                if indegree[nxt] == 0:
                    q.append(nxt)

    if len(result) < n:
        is_impossible = True
        
    if is_impossible:
        print('IMPOSSIBLE')
    elif is_unknown:
        print('?')
    else:
        print(*result)