from collections import deque
INF = int(1e9)

a, b = map(int, input().split())
q = deque()
q.append((a, 0))
result = INF
while q:
    now, count = q.popleft()

    if now == b:
        result = count
        break

    if now * 2 <= INF:
        q.append((now * 2, count + 1))
    if now * 10 + 1 <= INF:
        q.append((now * 10 + 1, count + 1))

if result == INF:
    print(-1)
else:
    print(result + 1)