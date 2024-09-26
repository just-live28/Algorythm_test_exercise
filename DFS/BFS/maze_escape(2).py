from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input())))
# (n, m)은 board[n-1][m-1], visited[n-1][m-1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board, a, b):
    q = deque()
    q.append((a, b))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 1 <= nx and nx <= n and 1 <= ny and ny <= m:
                if board[nx-1][ny-1] == 1:
                    board[nx-1][ny-1] = board[x-1][y-1] + 1
                    q.append((nx, ny))

bfs(board, 1, 1)

print(board[n-1][m-1])