board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

dir = [(1,0),(0,1),(1,1),(-1,1)]

def count_connected(board, x, y, dx, dy):
    color = board[x][y]
    count = 1
    left_x, left_y = x, y
    
    nx, ny = x + dx, y + dy
    while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
        count += 1
        nx, ny = nx + dx, ny + dy
    
    nx, ny = x - dx, y - dy
    while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
        count += 1
        left_x, left_y = nx, ny
        nx, ny = nx - dx, ny - dy
    
    return count, left_x, left_y
    
def check_five(board):
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue
            for dx, dy in dir:
                connected, target_x, target_y = count_connected(board, i, j, dx, dy)
                if connected == 5:
                    return board[i][j], target_x, target_y
    return 0, -1, -1

win_color, win_x, win_y = check_five(board)

if win_color == 0:
    print(0)
else:
    print(win_color)
    print(win_x+1, win_y+1)