from collections import deque
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
st, en = map(int, input().split())

q = deque()
q.append((0, st))
distance = [-1] * (n+1)
distance[st] = 0
routes = [[] for _ in range(n+1)]
while q:
    dist, now = q.popleft()

    if dist < distance[now]:
        continue

    for nxt, length in graph[now]:
        cost = dist + length

        if cost > distance[nxt]:
            distance[nxt] = cost
            routes[nxt] = [now]
            q.append((cost, nxt))
        elif cost == distance[nxt]:
            routes[nxt].append(now)

visited = set()
q.append(en)
result = 0
while q:
    now = q.popleft()

    if now == st:
        continue

    for pre in routes[now]:
        if (now, pre) not in visited:
            result += 1
            visited.add((now, pre))
            q.append(pre)

print(distance[en])
print(result)