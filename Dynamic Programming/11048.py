import copy

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# (x-1, y), (x, y-1), (x-1, y-1)
dir = [(-1, 0), (0, -1), (-1, -1)]

d = copy.deepcopy(board)
for i in range(n):
    for j in range(m):
        for dx, dy in dir:
            nx, ny = i + dx, j + dy

            if 0 <= nx < n and 0 <= ny < m:
                d[i][j] = max(d[i][j], d[nx][ny] + board[i][j])

print(d[n-1][m-1])