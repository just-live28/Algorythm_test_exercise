from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    shops = []
    for _ in range(n):
        x, y = map(int, input().split())
        shops.append((x, y))
    tx, ty = map(int, input().split())

    visited = [False] * n
    q = deque()
    q.append((hx, hy))
    enable = False
    while q:
        x, y = q.popleft()

        if abs(tx - x) + abs(ty - y) <= 1000:
            enable = True
            break

        for i in range(n):
            sx, sy = shops[i]

            if abs(sx - x) + abs(sy - y) <= 1000 and not visited[i]:
                visited[i] = True
                q.append((sx, sy))

    if enable:
        print('happy')
    else:
        print('sad')