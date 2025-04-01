import sys
sys.setrecursionlimit(10**5)

n = int(input())
board = []
for _ in range(n):
    board.append([int(x) for x in input()])

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    count = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and not visited[nx][ny]:
            count += dfs(nx, ny)
    
    return count
    
visited = [[False] * n for _ in range(n)]
area = 0
result = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            area += 1
            result.append(dfs(i, j))
result.sort()

print(area)
for i in result:
    print(i)