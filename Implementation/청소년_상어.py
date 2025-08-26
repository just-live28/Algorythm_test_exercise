import copy

board = []
for _ in range(4):
    line = list(map(int, input().split()))
    row = []
    for i in range(4):
        row.append([line[2*i], line[2*i + 1] - 1])
    board.append(row)

dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def find_fish(arr, fnum):
    for a in range(4):
        for b in range(4):
            if arr[a][b][0] == fnum:
                return a, b
    
    return None

def move_fishes(board, sx, sy):
    for fnum in range(1, 17):
        fish_loc = find_fish(board, fnum)
        if fish_loc == None:
            continue
        
        fx, fy = fish_loc
        fdir = board[fx][fy][1]
        for _ in range(8):
            nx, ny = fx + dir[fdir][0], fy + dir[fdir][1]
            
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy):
                # 좌표 교환 및 회전 종료
                board[fx][fy][1] = fdir
                board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]                
                break
            
            fdir = (fdir + 1) % 8

def routine(tx, ty, board, score):
    global max_score
    board = copy.deepcopy(board)
    
    # 섭취 및 탈취
    score += board[tx][ty][0]
    
    board[tx][ty][0] = 0
    sdir = board[tx][ty][1]
    
    # 물고기 이동
    move_fishes(board, tx, ty)
    
    # 상어 이동
    sx, sy = tx + dir[sdir][0], ty + dir[sdir][1]
    moved = False
    while 0 <= sx < 4 and 0 <= sy < 4:
        if board[sx][sy][0] > 0:
            moved = True
            routine(sx, sy, board, score)
            
        sx += dir[sdir][0]
        sy += dir[sdir][1]
    
    if not moved:
        max_score = max(max_score, score)

max_score = 0
routine(0, 0, board, 0)

print(max_score)