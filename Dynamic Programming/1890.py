n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int ,input().split())))
    
d = [[0] * n for _ in range(n)]
if board[0][0] < n:
    d[0][board[0][0]] = 1
    d[board[0][0]][0] = 1

for i in range(n):
    for j in range(n):
        for step_x in range(1, 100):
            prev_x = i - step_x
            if prev_x < 0:
                break
            if prev_x + board[prev_x][j] == i:
                d[i][j] += d[prev_x][j]
        for step_y in range(1, 100):
            prev_y = j - step_y
            if prev_y < 0:
                break
            if prev_y + board[i][prev_y] == j:
                d[i][j] += d[i][prev_y]

print(d[n-1][n-1])