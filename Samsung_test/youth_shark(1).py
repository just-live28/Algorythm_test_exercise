import copy

board = [[None] * 4 for _ in range(4)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
result = 0

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = (line[2*j], line[2*j+1] -1)

def find_fish(array, num):
    for a in range(4):
        for b in range(4):
            if array[a][b][0] == num:
                return (a, b)
    return None

def move_fish(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position != None:
            fx, fy = position
            fnum, fdir = array[fx][fy]
            for i in range(8):
                nx, ny = fx + dx[fdir], fy + dy[fdir]
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[fx][fy] = (fnum, fdir)
                        array[fx][fy], array[nx][ny] = array[nx][ny], array[fx][fy]
                        break
                fdir = (fdir + 1) % 8

def possible_shark_move(array, now_x, now_y):
    positions = []
    sdir = array[now_x][now_y][1]
    for _ in range(3):
        now_x += dx[sdir]
        now_y += dy[sdir]
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)
    
    fnum, fdir = array[now_x][now_y]
    total += fnum
    array[now_x][now_y] = (-1, fdir)
    
    move_fish(array, now_x, now_y)
    
    positions = possible_shark_move(array, now_x, now_y)
    if len(positions) == 0:
        result = max(result, total)
        return
    
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

dfs(board, 0, 0, 0)
print(result) 