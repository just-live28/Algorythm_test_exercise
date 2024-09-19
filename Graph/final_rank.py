import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

results = []
for _ in range(t):
    n = int(input())
    prev_rank = list(map(int, input().split()))

    graph = [[False] * (n+1) for _ in range(n+1)]
    indegree = [0] * (n+1)

    for i in range(n):
        for j in range(i+1, n):
            graph[prev_rank[i]][prev_rank[j]] = True
            indegree[prev_rank[j]] += 1
        
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[b] += 1
            indegree[a] -= 1

    cycle = False
    each_1 = True
    result = []

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    for a in range(n):
        
        if len(q) == 0:
            cycle = True
            break
        elif len(q) >= 2:
            each_1 = False
            break
        else:
            now = q.popleft()
            result.append(now)
            
            for i in range(1, n+1):
                if graph[now][i]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)

    if cycle:
        results.append(["IMPOSSIBLE"])
    elif not each_1:
        results.append(["?"])
    else:
        results.append(result)

for result in results:
    if len(result) == 1:
        print(result[0])
    else:
        for i in result:
            print(i, end=' ')
        print()
