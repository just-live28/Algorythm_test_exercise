n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 0 천장 1 바닥 2 북 3 남 4 서 5 동
dice = [0, 0, 0, 0, 0, 0]
plans = list(map(int, input().split()))
for plan in plans:
    if plan == 1 and y+1 < m:
        y += 1
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    elif plan == 2 and y-1 >= 0:
        y -= 1
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[5], dice[0], dice[1]
    elif plan == 3 and x-1 >= 0:
        x -= 1
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    elif plan == 4 and x+1 < n:
        x += 1
        dice[0], dice[1], dice[3], dice[2] = dice[2], dice[3], dice[0], dice[1]
    else:
        continue
    
    print(dice[0])

    if board[x][y] == 0:
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0