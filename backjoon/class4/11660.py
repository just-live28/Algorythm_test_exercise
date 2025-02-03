import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

d = [[0] * n for _ in range(n)]
d[0][0] = board[0][0]
for i in range(1, n):
    d[0][i] = d[0][i-1] + board[0][i]
for i in range(1, n):
    d[i][0] = d[i-1][0] + board[i][0]

for i in range(1, n):
    for j in range(1, n):
        d[i][j] = d[i-1][j] + d[i][j-1] + board[i][j] - d[i-1][j-1]

def cal_sum(x1, y1, x2, y2):
    if x1 == 0 and y1 == 0:
        return d[x2][y2]
    elif x1 == 0 and y1 > 0:
        return d[x2][y2] - d[x2][y1-1]
    elif x1 > 0 and y1 == 0:
        return d[x2][y2] - d[x1-1][y2]
    else:
        return d[x2][y2] - d[x2][y1-1] - d[x1-1][y2] + d[x1-1][y1-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(cal_sum(x1-1, y1-1, x2-1, y2-1))