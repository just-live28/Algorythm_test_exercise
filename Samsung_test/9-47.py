import copy

directions = [(0,0), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]

board = [[0] * 4 for _ in range(4)]
fishs = [[0] * 3 for _ in range(17)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        n, d = line[2*j: 2*(j+1)]
        board[i][j] = n
        fishs[n] = [d, i, j]

init_num = board[0][0]
max_score = init_num
s_dir = fishs[init_num][0]
fishs[init_num] = None
board[0][0] = 99

def move_fishs(board, fishs):
    for i in range(1, 17):
        if fishs[i] == None:
            continue
        now_dir, fx, fy = fishs[i]
        for _ in range(8):
            nx, ny = fx + directions[now_dir][0], fy + directions[now_dir][1]
            if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] != 99:
                if board[nx][ny] == 0:
                    # board 서로 교환. fishs 본인거 변경
                    fishs[i] = [now_dir, nx, ny]
                    board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
                else:
                    n_num = board[nx][ny]
                    nl = fishs[n_num][0]
                    fishs[i], fishs[n_num] = [now_dir, nx, ny], [nl, fx, fy]
                    board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]        
                break
            now_dir = (now_dir % 8) + 1

def execute_simulator(score, board, fishs, sx, sy, s_dir):
    global max_score
    
    move_fishs(board, fishs)
    
    moved = False
    for step in range(1, 4):
        nx, ny = sx + directions[s_dir][0] * step, sy + directions[s_dir][1] * step
        
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= board[nx][ny] <= 16:
            moved = True
            
            nboard = copy.deepcopy(board)
            nfishs = copy.deepcopy(fishs)
            
            target_num = board[nx][ny]
            nboard[sx][sy] = 0
            nscore = score + target_num
            ndir = nfishs[target_num][0]
            nfishs[target_num] = None
            nboard[nx][ny] = 99
            
            execute_simulator(nscore, nboard, nfishs, nx, ny, ndir)
    
    if not moved:
        max_score = max(score, max_score)
            
execute_simulator(max_score, board, fishs, 0, 0, s_dir)

print(max_score)