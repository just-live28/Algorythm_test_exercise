from collections import deque
INF = int(1e9)

# n 사다리 m 뱀
n, m = map(int, input().split())
ladders = dict()
snakes = dict()

for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snakes[x] = y

q = deque()
q.append((0, 1))
visited = [INF] * 101
visited[1] = 0

while q:
    cnt, now = q.popleft()

    if now == 100:
        print(cnt)
        break

    for i in range(1, 7):
        nxt = now + i
        if nxt <= 100 and cnt+1 < visited[nxt]:
            visited[nxt] = cnt+1
            if nxt in ladders:
                q.append((cnt+1, ladders[nxt]))
            elif nxt in snakes:
                q.append((cnt+1, snakes[nxt]))
            else:
                q.append((cnt+1, nxt))