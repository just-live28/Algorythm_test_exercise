dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def go(x, y):
    if d[x][y] != -1:
        return d[x][y]
    
    d[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > board[x][y]:
            d[x][y] = max(d[x][y], go(nx, ny) + 1)
    
    return d[x][y]

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
d = [[-1] * n for _ in range(n)]

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, go(i, j))

print(result)