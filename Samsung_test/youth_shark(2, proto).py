import copy

board = [[0]*4 for _ in range(4)]
fishs = [(0, 0, 0)] * 17

for a in range(4):
    line = list(map(int, input().split()))
    for b in range(4):
        board[a][b] = line[2*b]
        fishs[line[2*b]] = (line[2*b+1], a, b)

dir = [(), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def move_fish(board, fishs):
    for i in range(1, 17):
        if fishs[i] == None:
            continue
        
        fl, fx, fy = fishs[i]
        
        for _ in range(8):
            nx, ny = fx + dir[fl][0], fy + dir[fl][1]
            
            if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] != 99:
                if board[nx][ny] == 0:
                    fishs[i] = (fl, nx, ny)
                    board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
                else:
                    n_num = board[nx][ny]
                    nl = fishs[n_num][0]
                    fishs[i], fishs[n_num] = (fl, nx, ny), (nl, fx, fy)
                    board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
                break
        
            fl = fl % 8 + 1
            
now_score, now_x, now_y, now_l = 0, 0, 0, 0

init_num = board[0][0]
now_l = fishs[init_num][0]

fishs[init_num] = None
board[0][0] = 99
now_score += init_num

result = []

def routine(board, fishs, sx, sy, sl, score):
    nboard = copy.deepcopy(board)
    nfishs = copy.deepcopy(fishs)
    
    move_fish(nboard, nfishs)
    
    moved = False
    for step in range(1, 4):
        nx, ny = sx + step * dir[sl][0], sy + step * dir[sl][1]
        
        if 0 <= nx < 4 and 0 <= ny < 4 and nboard[nx][ny] != 0:
            moved = True
            
            n_num = nboard[nx][ny]
            nl = nfishs[n_num][0]
            
            origin_nfishs_nnum = nfishs[n_num]
            origin_nboard_nxny = nboard[nx][ny]
            origin_nboard_sxsy = nboard[sx][sy]
            
            nfishs[n_num] = None
            nboard[nx][ny] = 99
            nboard[sx][sy] = 0
            
            routine(nboard, nfishs, nx, ny, nl, score + n_num)
            
            nfishs[n_num] = origin_nfishs_nnum
            nboard[nx][ny] = origin_nboard_nxny
            nboard[sx][sy] = origin_nboard_sxsy
    
    if not moved:
        result.append(score)
        return

routine(board, fishs, now_x, now_y, now_l, now_score)

print(max(result))