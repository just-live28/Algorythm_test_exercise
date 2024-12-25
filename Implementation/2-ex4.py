n, m = map(int, input().split())
x, y, dir = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]
visited[x][y] = True

count = 1
while True:
    move = False
    for _ in range(4):
        dir = (dir - 1) % 4
        nx, ny = x + dx[dir], y + dy[dir]
        
        if 0 < nx < n and 0 < ny < m and board[nx][ny] == 0 and visited[nx][ny] == False:
            move = True
            visited[nx][ny] = True
            x, y = nx, ny
            count += 1
            break
    
    if move:
        continue
    
    nx, ny = x - dx[dir], y - dy[dir]
    if board[nx][ny] == 1:
        break
    else:
        if visited[nx][ny] == False:
            visited[nx][ny] = True
            x, y = nx, ny
            count += 1
        else:
            x, y = nx, ny

print(count)