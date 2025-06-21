from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))

    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            indegree[arr[j]] += 1
            graph[arr[i]][arr[j]] = True

    m = int(input())
    for _ in range(m):
        # a 고순위 b 저순위
        a, b = map(int, input().split())

        if graph[a][b] == True:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1
            
    q = deque()

    result = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    cycle = False
    while q:
        if len(q) > 1:
            cycle = True
            break

        now = q.popleft()
        result.append(now)

        for nxt in range(1, n+1):
            if graph[now][nxt]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

    if len(result) < n:
        print('IMPOSSIBLE')
    elif cycle:
        print('?')
    else:
        print(*result)