import copy

board = [[] for _ in range(4)]

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        board[i].append([line[j * 2], line[j * 2 + 1] - 1])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

max_score = 0

def find_fish(board, index):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == index:
                return (i, j)
    return None


def move_fishs(board, sx, sy):
    for i in range(1, 17):
        position = find_fish(board, i)
        if position != None:
            fx, fy = position
            fdir = board[fx][fy][1]

            for _ in range(8):
                nx, ny = fx + dx[fdir], fy + dy[fdir]

                if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                    board[fx][fy][1] = fdir
                    board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
                    break

                fdir = (fdir + 1) % 8

def find_positions(board, sx, sy):
    positions = []

    sdir = board[sx][sy][1]
    for i in range(1, 4):
        nx, ny = sx + i * dx[sdir], sy + i * dy[sdir]

        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny][0] != -1:
            positions.append((nx, ny))

    return positions

def routine(board, sx, sy, score):
    global max_score
    board = copy.deepcopy(board)

    score += board[sx][sy][0]
    board[sx][sy][0] = -1

    move_fishs(board, sx, sy)

    positions = find_positions(board, sx, sy)

    if len(positions) == 0:
        max_score = max(max_score, score)
        return

    for px, py in positions:
        routine(board, px, py, score)

routine(board, 0, 0, 0)
print(max_score)