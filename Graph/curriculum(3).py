# i가 더 상위 차수다
import copy
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

times = [0] * (n+1)
for i in range(1, n+1):
    line = list(map(int, input().split()))

    times[i] = line[0]
    for j in line[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

result = copy.deepcopy(times)
while q:
    now = q.popleft()

    for i in graph[now]:
        # 상위 차수 시간 + 여태까지 들었던 하위 차수 시간 중 가장 긴 시간
        result[i] = max(result[i], times[i] + result[now])
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

print(result)





