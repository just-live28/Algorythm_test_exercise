from collections import deque

tc = int(input())
for _ in range(tc):
    n = int(input())
    last_rank = list(map(int, input().split()))

    indegree = [0] * (n+1)
    for i in range(n):
        indegree[last_rank[i]] = i

    graph = [[False] * (n+1) for _ in range(n+1)]
    for i in range(n-1):
        for j in last_rank[i+1:]:
            graph[last_rank[i]][j] = True

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        
        if graph[a][b] == True:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[b] += 1
            indegree[a] -= 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    is_question = False
    result = []
    while q:
        if len(q) > 1:
            is_question = True
            break
        
        now = q.popleft()
        result.append(now)
        for i in range(1, n+1):
            if graph[now][i] == True:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if len(result) < n:
        print("IMPOSSIBLE")
    elif is_question == True:
        print("?")
    else:
        for i in result:
            print(i, end=' ')