n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# dir 0 가로 1 세로
def dfs(block_count, score, x, y, dir):
    global total

    if block_count == 4:
        total = max(total, score)
        return
    
    # ㅗ 모양
    if block_count == 2:
        # 가로로 온 경우, 세로로 위 아래
        if dir == 0:
            if 0 <= x-1 < n and 0 <= x+1 < n:
                dfs(block_count+2, score + board[x-1][y] + board[x+1][y], 0, 0, -1)
        # 세로로 온 경우, 가로로 위 아래
        elif dir == 1:
            if 0 <= y-1 < m and 0 <= y+1 < m:
                dfs(block_count+2, score + board[x][y-1] + board[x][y+1], 0, 0, -1)

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True

            if block_count == 1:
                if d == 0 or d == 1:
                    dfs(block_count + 1, score + board[nx][ny], nx, ny, 1)
                elif d == 2 or d == 3:
                    dfs(block_count + 1, score + board[nx][ny], nx, ny, 0)
            else:
                dfs(block_count + 1, score + board[nx][ny], nx, ny, -1)
            visited[nx][ny] = False

total = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(1, board[i][j], i, j, -1)
        visited[i][j] = False

print(total)