from collections import deque

tc = int(input())

results = []
for _ in range(tc):
    n = int(input())

    prev_rank = list(map(int, input().split()))

    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            indegree[prev_rank[j]] += 1
            graph[prev_rank[i]][prev_rank[j]] = True

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())

        if graph[a][b] == True:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    is_unknown = False
    result = []
    while q:
        if len(q) > 1:
            is_unknown = True
            break

        now = q.popleft()
        result.append(now)

        for i in range(1, n + 1):
            if graph[now][i] == True:
                indegree[i] -= 1

                if indegree[i] == 0:
                    q.append(i)

    if is_unknown:
        results.append('?')
    elif len(result) < n:
        results.append('IMPOSSIBLE')
    else:
        results.append(result)

for result in results:
    if isinstance(result, list):
        for i in result:
            print(i, end=' ')
        print()
    else:
        print(result)