from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

n, m = map(int, input().split())
board = [[-1] * m for _ in range(n)]

sharks = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 1:
            sharks.append((i, j))

q = deque()
for shark in sharks:
    board[shark[0]][shark[1]] = 0
    q.append((0, shark[0], shark[1]))

max_length = 0
while q:
    length, sx, sy = q.popleft()

    for i in range(8):
        nx, ny = sx + dx[i], sy + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == -1:
            board[nx][ny] = length + 1
            max_length = max(max_length, length + 1)
            q.append((length + 1, nx, ny))

print(max_length)