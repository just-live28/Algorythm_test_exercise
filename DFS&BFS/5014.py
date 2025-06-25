# f 최고층 s 현재층 g 목표층 u 위 d 아래
from collections import deque
INF = int(1e9)

f, s, g, u, d = map(int, input().split())
visited = [INF] * (f+1)
visited[s] = 0
q = deque()
q.append((0, s))
result = INF
while q:
    count, now = q.popleft()

    if now == g:
        result = count
        break

    if now + u <= f and count + 1 < visited[now + u]:
        visited[now + u] = count + 1
        q.append((count + 1, now + u))
    
    if now - d >= 1 and count + 1 < visited[now - d]:
        visited[now - d] = count + 1
        q.append((count + 1, now - d))

if result == INF:
    print('use the stairs')
else:
    print(result)