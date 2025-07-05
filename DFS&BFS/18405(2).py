import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())
board = [None]
viruses = []
for i in range(1, n+1):
    line = list(map(int, input().split()))
    board.append([0] + line)
    for j in range(1, n+1):
        if line[j-1] != 0:
            viruses.append((line[j-1], i, j))
s, x, y = map(int, input().split())

q = []
for vnum, vx, vy in viruses:
    heapq.heappush(q, (0, vnum, vx, vy))

while q:
    t, vnum, vx, vy = heapq.heappop(q)

    if t == s:
        break

    for i in range(4):
        nx, ny = vx + dx[i], vy + dy[i]

        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] == 0:
            board[nx][ny] = vnum
            heapq.heappush(q, (t+1, vnum, nx, ny))

print(board[x][y])