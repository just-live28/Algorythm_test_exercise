board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

dx = [-1,0,1,1]
dy = [1,1,1,0]

def count_omok(x, y, d):
    color = board[x][y]
    count = 1
    left_x, left_y = x, y
    
    nx, ny = x + dx[d], y + dy[d]
    while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
        count += 1
        nx, ny = nx + dx[d], ny + dy[d]
    
    nx, ny = x - dx[d], y - dy[d]
    while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
        count += 1
        left_x, left_y = nx, ny
        nx, ny = nx - dx[d], ny - dy[d]
    
    return count, left_x, left_y

def check_board(board):
    for a in range(19):
        for b in range(19):
            if board[a][b] == 0:
                continue
            
            for i in range(4):
                count, left_x, left_y = count_omok(a, b ,i)
                if count == 5:
                    return board[a][b], left_x, left_y
                
    return 0, -1, -1

win_color, win_x, win_y = check_board(board)

print(win_color)
if win_color != 0:
    print(win_x + 1, win_y + 1)