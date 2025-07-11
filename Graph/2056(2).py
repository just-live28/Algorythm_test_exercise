from collections import deque
import copy
n = int(input())

times = [0] * (n+1)
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for i in range(1, n+1):
    line = list(map(int, input().split()))
    times[i] = line[0]

    if i == 1:
        continue

    for pre in line[2:]:
        indegree[i] += 1
        graph[pre].append(i)

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

d = copy.deepcopy(times)
while q:
    now = q.popleft()

    for nxt in graph[now]:
        d[nxt] = max(d[nxt], d[now] + times[nxt])

        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print(max(d))