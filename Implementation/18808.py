n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]

def count_filled_space(board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                count += 1
    return count
            
def rotate(sticker):
    row = len(sticker)
    col = len(sticker[0])
    rotated_sticker = [[0] * row for _ in range(col)]
    
    for i in range(row):
        for j in range(col):
            rotated_sticker[j][row-i-1] = sticker[i][j]
    return rotated_sticker

def sticker_on(sticker, x, y, row, col):
    for i in range(x, x + row):
        for j in range(y, y + col):
            if sticker[i-x][j-y] == 1:
                board[i][j] += 1

def valid_sticker(x, y, row, col):
    for i in range(x, x + row):
        for j in range(y, y + col):
            if board[i][j] == 2:
                return False
    return True

def sticker_off(sticker, x, y, row, col):
    for i in range(x, x + row):
        for j in range(y, y + col):
            if sticker[i-x][j-y] == 1:
                board[i][j] -= 1
                
def get_on_sticker(sticker):
    for _ in range(4):
        row = len(sticker)
        col = len(sticker[0])
        for a in range(n-row+1):
            for b in range(m-col+1):
                sticker_on(sticker, a, b, row, col)
                if valid_sticker(a, b, row, col):
                    return
                sticker_off(sticker, a, b, row, col)
        sticker = rotate(sticker)

for _ in range(k):
    r, c = map(int, input().split())
    sticker = []
    for _ in range(r):
        sticker.append(list(map(int, input().split())))
    get_on_sticker(sticker)

print(count_filled_space(board))