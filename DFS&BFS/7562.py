from collections import deque

moves = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]

tc = int(input())
for _ in range(tc):
    i = int(input())
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    visited = [[False] * i for _ in range(i)]
    visited[sx][sy] = True
    q = deque()
    q.append((0, sx, sy))
    while q:
        cnt, x, y = q.popleft()

        if (x, y) == (tx, ty):
            print(cnt)
            break

        for move in moves:
            nx, ny = x + move[0], y + move[1]

            if 0 <= nx < i and 0 <= ny < i and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((cnt + 1, nx, ny))