n = int(input())
init_board = []
for _ in range(n):
    init_board.append(list(map(int, input().split())))

def move_board(board):
    moved_board = []
    for i in range(n):
        line = board[i]
        tilted = [0] * n
        idx = 0
        for j in range(n):
            if line[j] == 0:
                continue
            if tilted[idx] == 0:
                tilted[idx] = line[j]
            elif tilted[idx] == line[j]:
                tilted[idx] *= 2
                idx += 1
            else:
                idx += 1
                tilted[idx] = line[j]
        moved_board.append(tilted)
    return moved_board

def rotate(board):
    new_board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[j][-(i+1)] = board[i][j]
    return new_board

def func(k, board):
    global max_block
    if k == 5:
        max_block = max(max_block, max([max(line) for line in board]))
        return

    for _ in range(4):
        board = rotate(board)
        func(k+1, move_board(board))

max_block = 0
func(0, init_board)
print(max_block)