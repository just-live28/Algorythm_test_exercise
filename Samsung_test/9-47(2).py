import copy

board = [[[0,0]] * 4 for _ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = [line[2*j], line[2*j + 1]]

directions = [None, (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]

def find_fish(board, target):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == target:
                return i, j
    return None

def move_fishes(board):
    for i in range(1, 17):
        position = find_fish(board, i)
        if find_fish(board, i) == None:
            continue
        fx, fy = position
        fnum, fdir = board[fx][fy]
        for _ in range(8):
            nx, ny = fx + directions[fdir][0], fy + directions[fdir][1]
            if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny][0] != 99:
                board[fx][fy], board[nx][ny] = board[nx][ny], [fnum, fdir]
                break
            fdir = fdir % 8 + 1

def find_targets(board, sx, sy, sdir):
    targets = []
    for _ in range(3):
        sx += directions[sdir][0]
        sy += directions[sdir][1]
        if 0 <= sx < 4 and 0 <= sy < 4 and 1 <= board[sx][sy][0] <= 16:
            targets.append((sx, sy))
    return targets

def routine(board, tx, ty, score):
    global max_score
    board = copy.deepcopy(board)
    # target_dir => sdir
    target_num, target_dir = board[tx][ty]
    board[tx][ty][0] = 99
    score += target_num
    
    move_fishes(board)
    
    targets = find_targets(board, tx, ty, target_dir)
    
    if len(targets) == 0:
        max_score = max(max_score, score)
        return
    
    board[tx][ty][0] = 0
    for nx, ny in targets:
        routine(board, nx, ny, score)  

max_score = 0
routine(board, 0, 0, 0)
print(max_score)