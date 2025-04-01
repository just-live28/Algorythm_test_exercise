import sys
sys.setrecursionlimit(10**5)

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count, visited):
    global max_value
    movable = False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and (visited & (1 << (ord(board[nx][ny]) - 65))) == 0:
            movable = True
            dfs(nx, ny, count + 1, visited | (1 << (ord(board[nx][ny]) - 65)))
    
    if not movable:
        max_value = max(max_value, count)
    
max_value = 0
dfs(0, 0, 1, 0 | (1 << (ord(board[0][0]) - 65)))
print(max_value)