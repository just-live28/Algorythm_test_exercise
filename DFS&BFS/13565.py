from collections import deque

m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append([int(x) for x in input()])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(visited, tx, ty):
    q = deque()
    q.append((tx, ty))
    visited[tx][ty] = True

    while q:
        x, y = q.popleft()

        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]

            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

visited = [[False] * n for _ in range(m)]
for i in range(n):
    if board[-1][i] == 0:
        bfs(visited, m-1, i)

enable = False
for i in range(n):
    if visited[0][i] == True:
        enable = True
        break

if enable:
    print('YES')
else:
    print('NO')