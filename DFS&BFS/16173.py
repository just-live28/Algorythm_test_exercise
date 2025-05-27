from collections import deque

dx = [0, 1]
dy = [1, 0]

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

q = deque()
q.append((0, 0))
enable = False
while q:
    x, y = q.popleft()

    if board[x][y] == -1:
        enable = True
        break
    elif board[x][y] == 0:
        continue

    for i in range(2):
        nx, ny = x + board[x][y] * dx[i], y + board[x][y] * dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            q.append((nx, ny))

if enable:
    print("HaruHaru")
else:
    print("Hing")