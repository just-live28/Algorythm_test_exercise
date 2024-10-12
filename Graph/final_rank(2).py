# 높은 등수 : 낮은 차수
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())

    indegree = [0] * (n+1)

    graph = [[False]*(n+1) for _ in range(n+1)]

    line = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[line[i]][line[j]] = True
            indegree[line[j]] += 1

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            
            indegree[b] += 1
            indegree[a] -= 1

    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    cycle = False
    unfind = False
    result = []
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break

        now = q.popleft()
        result.append(now)
        
        for i in range(1, n+1):
            if graph[now][i]:
                indegree[i] -= 1
                
                if indegree[i] == 0:
                    q.append(i)
        
        if len(q) > 1:
            unfind = True
            break

    if cycle:
        print('IMPOSSIBLE')
    elif unfind:
        print('?')
    else:
        for i in result:
            print(i, end=' ')
        print()