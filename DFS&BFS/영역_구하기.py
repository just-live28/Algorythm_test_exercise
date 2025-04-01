import sys
sys.setrecursionlimit(10**5)

m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for a in range(sy, ey):
        for b in range(sx, ex):
            board[a][b] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
        
def dfs(x, y):
    visited[x][y] = True
    count = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0 and not visited[nx][ny]:
            count += dfs(nx, ny)

    return count

visited = [[False] * n for _ in range(m)]
result = []
area = 0
for a in range(m):
    for b in range(n):
        if board[a][b] == 0 and not visited[a][b]:
            area += 1
            result.append(dfs(a, b))

result.sort()
print(area)
print(*result)