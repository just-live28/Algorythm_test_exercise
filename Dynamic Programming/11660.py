# sums[x2, y2] - sums[x1, y1] + board[x1, y1]
# sums[x][y] = sums[x][y-1] + sums[x-1][y] + board[x][y] - sums[x-1][y-1]

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

sums = [[0] * n for _ in range(n)]
sums[0][0] = board[0][0]
for i in range(1, n):
    sums[0][i] = sums[0][i-1] + board[0][i]
    sums[i][0] = sums[i-1][0] + board[i][0]

for i in range(1, n):
    for j in range(1, n):
        sums[i][j] = sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1] + board[i][j]

for _ in range(m):
    line = list(map(int, input().split()))
    x1, y1 = line[0]-1 , line[1]-1
    x2, y2 = line[2]-1, line[3]-1
    
    result = sums[x2][y2]
    if y1 > 0:
        result -= sums[x2][y1-1]
    if x1 > 0:
        result -= sums[x1-1][y2]
    if y1 > 0 and x1 > 0:
        result += sums[x1-1][y1-1]
        
    print(result)