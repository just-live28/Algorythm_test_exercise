from collections import deque

n = int(input())
time = [0] * (n+1)

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    line = list(map(int, input().split()))
    time[i] = line[0]
    m = line[1]
    for j in range(m):
        indegree[i] += 1
        graph[line[j + 2]].append(i)

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

d = [0] * (n+1)
for i in range(1, n+1):
    d[i] = time[i]

while q:
    now = q.popleft()
    
    for nxt in graph[now]:
        d[nxt] = max(d[nxt], d[now] + time[nxt])
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print(max(d))