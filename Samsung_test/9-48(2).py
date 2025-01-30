n, m, k = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#board[x][y] = snum | 0
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
# direction[snum -1] = sdir
direction = list(map(int, input().split()))
# priority[snum -1][sdir - 1] = [2, 3, 1, 4](예시)
priority = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        priority[i].append(list(map(int, input().split())))
# peromon[x][y] = [snum, remain_time]
peromon = [[[0,0]] * n for _ in range(n)]

def update_peromon():
    for i in range(n):
        for j in range(n):
            if peromon[i][j][1] > 0:
                peromon[i][j][1] -= 1
            
            if board[i][j] != 0:
                peromon[i][j] = [board[i][j], k]

def move_shark():
    temp_board = [[0] * n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                continue
            sdir = direction[board[x][y] -1]
            moved = False
            for i in priority[board[x][y] -1][sdir - 1]:
                nx, ny = x + dx[i-1], y + dy[i-1]  
                if 0 <= nx < n and 0 <= ny < n and peromon[nx][ny][1] == 0:
                    if temp_board[nx][ny] == 0:
                        temp_board[nx][ny] = board[x][y]
                    else:
                        temp_board[nx][ny] = min(temp_board[nx][ny], board[x][y])
                    direction[board[x][y] -1] = i
                    moved = True
                    break
            if not moved:
                for i in priority[board[x][y] -1][sdir - 1]:
                    nx, ny = x + dx[i-1], y + dy[i-1]  
                    if 0 <= nx < n and 0 <= ny < n and peromon[nx][ny][0] == board[x][y]:
                        temp_board[nx][ny] = board[x][y]
                        direction[board[x][y] -1] = i
                        break
    return temp_board

time = 0
while True:
    update_peromon()
    temp_board = move_shark()
    board = temp_board
    time += 1
    
    checked = True
    for i in range(n):
        for j in range(n):
            if board[i][j] > 1:
                checked = False
    
    if checked:
        print(time)
        break
    
    if time >= 1000:
        print(-1)
        break