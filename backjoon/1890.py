n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

d = [[0] * n for _ in range(n)]
if board[0][0] < n:
    d[0][board[0][0]] = 1
    d[board[0][0]][0] = 1

for i in range(n):
    for j in range(n):
        for jump in range(1, j+1):
            if jump == board[i][j-jump]:
                d[i][j] += d[i][j-jump]
        for jump in range(1, i+1):
            if jump == board[i-jump][j]:
                d[i][j] += d[i-jump][j]

print(d[n-1][n-1])