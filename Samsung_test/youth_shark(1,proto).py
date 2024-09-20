import copy


dir = [(0,0), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]

board = [[(0,0)] * 4 for _ in range(4)]
fishs = [(-1,-1)] * 17
max_num = 0
init_sx, init_sy = 0, 0

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = (line[2*j], line[2*j + 1])
        fishs[line[2*j]] = (i, j)

# (0,0)의 물고기가 먹힘
init_num, init_dir = board[0][0]
board[0][0] = (99, init_dir)
fishs[init_num] = (-1, -1)
max_num += init_num

def move_fish(each_fishs, each_board):
    for i in range(1, 17):
        fx, fy = each_fishs[i]
        #먹힌 물고기면 패스
        if fx == -1:
            continue
        fnum, fdir = each_board[fx][fy]
        
        for _ in range(8):
            nx, ny = fx + dir[fdir][0], fy + dir[fdir][1]
            # 경계 너머이거나 상어를 만났을 때
            if 0 <= nx and nx < 4 and 0 <= ny and ny < 4 and each_board[nx][ny][0] != 99:
                nnum, ndir = each_board[nx][ny]
                each_board[fx][fy], each_board[nx][ny] = (nnum, ndir), (fnum, fdir)
                each_fishs[fnum], each_fishs[nnum] = (nx,ny), (fx,fy)
                break             
            fdir = (fdir + 1) % 8
    return each_board, each_fishs

def routine(board, fishs, sx, sy, sdir, total_num):
    global max_num
    
    copied_board = copy.deepcopy(board)
    copied_fishs = copy.deepcopy(fishs)
    # 물고기 턴
    board, fishs = move_fish(copied_fishs, copied_board)
    # 상어 턴
    moved = False
    for step in range(1, 4):
        nx, ny =  sx + dir[sdir][0] * step, sy + dir[sdir][1] * step
        if 0 <= nx and nx < 4 and 0 <= ny and ny < 4 and board[nx][ny][0] > 0:
            moved = True
            fnum, fdir = board[nx][ny]
            
            # 상어가 물고기를 섭취
            new_board = copy.deepcopy(board)
            new_fishs = copy.deepcopy(fishs)
            new_board[sx][sy] = (0, 0)
            new_board[nx][ny] = (99, fdir)
            new_fishs[fnum] = (-1, -1)
            
            routine(new_board, new_fishs, nx, ny, fdir, total_num + fnum)
            
    if not moved:
        max_num = max(max_num, total_num)

routine(board, fishs, init_sx, init_sy, init_dir, init_num)

print(max_num)