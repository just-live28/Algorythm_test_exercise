import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    board = []
    for _ in range(2):
        board.append(list(map(int, input().split())))

    if n == 1:
        print(max(board[0][0], board[1][0]))
    elif n == 2:
        print(max(board[0][0] + board[1][1], board[1][0] + board[0][1]))
    else:
        d = [[0] * n for _ in range(2)]
        d[0][0] = board[0][0]
        d[1][0] = board[1][0]
        d[0][1] = board[1][0] + board[0][1]
        d[1][1] = board[0][0] + board[1][1]

        for j in range(2, n):
            d[0][j] = max(d[0][j-1], max(d[0][j-2], d[1][j-2], d[1][j-1]) + board[0][j])
            d[1][j] = max(d[1][j-1], max(d[0][j-2], d[1][j-2], d[0][j-1]) + board[1][j])

        print(max(d[0][n-1], d[1][n-1]))