from collections import deque
INF = int(1e9)

n = int(input())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
for i in range(1, n+1):
    line = list(map(int, input().split()))
    time[i] = line[0]
    for j in line[1:]:
        if j == -1:
            continue
        indegree[i] += 1
        graph[j].append(i)

d = [0] * (n+1)
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        d[i] = time[i]
        q.append(i)

while q:
    now = q.popleft()
    
    for nxt in graph[now]:
        d[nxt] = max(d[nxt], d[now] + time[nxt])
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

for i in d[1:]:
    print(i)