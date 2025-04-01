import sys
sys.setrecursionlimit(10**5)

n = int(input())
normal_board = [[None] * n for _ in range(n)]
abnormal_board = [[None] * n for _ in range(n)]

for i in range(n):
    line = list(input())
    for j in range(n):
        if line[j] == 'G':
            normal_board[i][j] = 'G'
            abnormal_board[i][j] = 'R'
        else:
            normal_board[i][j] = line[j]
            abnormal_board[i][j] = line[j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(board, visited, color, x, y):
    visited[x][y] = True
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]    
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == color and not visited[nx][ny]:
            dfs(board, visited, color, nx, ny)

normal_area = 0
abnormal_area = 0
normal_visited = [[False] * n for _ in range(n)]
abnormal_visited = [[False] * n for _ in range(n)]
for a in range(n):
    for b in range(n):
        if not normal_visited[a][b]:
            normal_area += 1
            dfs(normal_board, normal_visited, normal_board[a][b], a, b)
        if not abnormal_visited[a][b]:
            abnormal_area += 1
            dfs(abnormal_board, abnormal_visited, abnormal_board[a][b], a, b)

print(normal_area, abnormal_area)