from collections import deque
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = [()]
for _ in range(n):
    board.append([0] + [int(x) for x in input()])

visited = [[[INF] * 2 for _ in range(m+1)] for _ in range(n+1)]
visited[1][1][0] = 1
q = deque()
q.append((1, 0, 1, 1))
while q:
    cnt, brk, x, y = q.popleft()

    if (x, y) == (n, m):
        if brk == 0:
            visited[x][y][0] = min(visited[x][y][0], cnt)
        else:
            visited[x][y][1] = min(visited[x][y][1], cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 1 <= nx <= n and 1 <= ny <= m:
            if board[nx][ny] == 0 and visited[nx][ny][brk] == INF:
                if brk == 0:
                    visited[nx][ny][0] = cnt + 1
                    q.append((cnt + 1, brk, nx, ny))
                elif brk == 1:
                    visited[nx][ny][1] = cnt + 1
                    q.append((cnt + 1, brk, nx, ny))
            else:
                if brk == 0 and visited[nx][ny][0] == INF:
                    visited[nx][ny][0] = cnt + 1
                    q.append((cnt + 1, 1, nx, ny))

result = min(visited[n][m][0], visited[n][m][1])
if result == INF:
    print(-1)
else:
    print(result)