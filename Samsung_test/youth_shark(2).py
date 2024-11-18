import copy

moves = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
max_result = 0

init_board = [[] for _ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        init_board[i].append([line[j * 2], line[(j * 2) + 1] - 1])


def find_fish(board, i):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == i:
                return (x, y)
    return None


def fish_move(board, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(board, i)

        if position != None:
            fx, fy = position
            fnum, fdir = board[fx][fy]

            for _ in range(8):
                nx, ny = fx + moves[fdir][0], fy + moves[fdir][1]

                if 0 <= nx < 4 and 0 <= ny < 4 and not (now_x == nx and now_y == ny):
                    board[fx][fy][1] = fdir
                    board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
                    break

                fdir = (fdir + 1) % 8


def shark_move(board, sx, sy, result):
    global max_result

    board = copy.deepcopy(board)
    result += board[sx][sy][0]
    board[sx][sy][0] = -1

    fish_move(board, sx, sy)

    positions = []
    sdir = board[sx][sy][1]
    for i in range(1, 4):
        nx, ny = sx + i * moves[sdir][0], sy + i * moves[sdir][1]

        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny][0] != -1:
            positions.append((nx, ny))

    if len(positions) == 0:
        max_result = max(max_result, result)
        return

    for px, py in positions:
        shark_move(board, px, py, result)


shark_move(init_board, 0, 0, 0)

print(max_result)
