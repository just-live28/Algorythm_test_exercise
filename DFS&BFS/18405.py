from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())
board = []
viruses = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] != 0:
            viruses.append((line[j], i, j))
    board.append(line)
viruses.sort()
s, x, y = map(int, input().split())
q = deque()
for vnum, vx, vy in viruses:
    q.append((0, vnum, vx, vy))
while q:
    t, vnum, vx, vy = q.popleft()
    if t == s:
        break
    for i in range(4):
        nx, ny = vx + dx[i], vy + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = vnum
            q.append((t+1, vnum, nx, ny))

print(board[x-1][y-1])