from collections import deque

n = int(input())

board = []
sx, sy, s_size = 0, 0, 2
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)

    for j in range(n):
        if line[j] == 9:
            sx, sy = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_target(board, sx, sy):
    q = deque()
    q.append((0, sx, sy))

    visited = [[False] * n for _ in range(n)]

    targets = []
    while q:
        l, x, y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True

                if board[nx][ny] > s_size:
                    continue
                else:
                    q.append((l + 1, nx, ny))
                    if board[nx][ny] != 0 and board[nx][ny] < s_size:
                        targets.append((l + 1, nx, ny))
    targets.sort(key=lambda x: (x[0], x[1], x[2]))
    return targets


t = 0
ate = 0
while True:
    targets = find_target(board, sx, sy)

    if len(targets) == 0:
        break

    tl, tx, ty = targets[0]

    t += tl
    board[sx][sy] = 0
    board[tx][ty] = 9
    sx, sy = tx, ty
    ate += 1

    if ate == s_size:
        s_size += 1
        ate = 0

print(t)