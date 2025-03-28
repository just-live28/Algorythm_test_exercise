from collections import deque

n = int(input())
m = int(input())

indgree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
component = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, k = map(int, input().split())
    indgree[x] += 1
    graph[y].append((x, k))

q = deque()
order = []
for i in range(1, n+1):
    if indgree[i] == 0:
        q.append(i)
        order.append(i)

while q:
    now = q.popleft()
    for i, quantity in graph[now]:
        indgree[i] -= 1
        component[i].append((now, quantity))
        if indgree[i] == 0:
            q.append(i)
            order.append(i)

need = [0] * (n+1)
need[n] = 1

for i in range(n-1, -1, -1):
    if need[order[i]] > 0 and component[order[i]]:
        for idx, quantity in component[order[i]]:
            need[idx] += quantity * need[order[i]]
        need[order[i]] = 0

for i in range(1, n+1):
    if need[i] > 0:
        print(i, need[i])