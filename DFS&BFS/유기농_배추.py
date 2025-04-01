import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)

# 가로 m 세로 n 배추개수 k
tc = int(input())
for _ in range(tc):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        board[b][a] = 1

    visited = [[False] * m for _ in range(n)]
    result = 0
    for a in range(n):
        for b in range(m):
            if board[a][b] == 1 and not visited[a][b]:
                result += 1
                dfs(a, b)

    print(result)