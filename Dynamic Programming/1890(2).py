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
        for step in range(1, n):
            if i - step >= 0 and i - step + board[i-step][j] == i:
                d[i][j] += d[i-step][j]
            if j - step >= 0 and j - step + board[i][j-step] == j:
                d[i][j] += d[i][j-step]

print(d[n-1][n-1])