# d[i][j]: (i, j)가 오른쪽 하단 모서리인 정사각형의 최대 길이
## 만약 board[i][j]가 1이라면, d[i][j] = min(d[i][j-1], d[i-1][j-1], d[i-1][j]) + 1
## board[i][j] 가 0이라면, d[i][j] = 0 (만들 수 없음)
# d[0][0]이 1이라면 1, 0이라면 0

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().strip())))

d = [[0] * m for _ in range(n)]
for i in range(n):
    if board[i][0] == 1:
        d[i][0] = 1
for j in range(m):
    if board[0][j] == 1:
        d[0][j] = 1
    
for i in range(1, n):
    for j in range(1, m):
        if board[i][j] == 0:
            continue
        
        d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1

max_length = 0
for i in range(n):
    for j in range(m):
        if d[i][j] > max_length:
            max_length = d[i][j]

print(max_length ** 2)