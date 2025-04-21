n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

clean_count = 0
while True:
    if board[r][c] == 0:
        clean_count += 1
        board[r][c] = -1

    dirt_exist = False
    for i in range(4):
        d = (d - 1) % 4
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 0:
            dirt_exist = True
            r, c = nr, nc
            break
            
    if not dirt_exist:
        nr, nc = r - dr[d], c - dc[d]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] != 1:
            r, c = nr, nc
        else:
            break

print(clean_count)