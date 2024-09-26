from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input())))

dx = [-1, 1, 0, 0]    
dy = [0, 0, -1, 1]

def bfs(board, a, b):
    q = deque()
    q.append((a, b))
    board[a][b] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < m:
                if board[nx][ny] == 0:
                   board[nx][ny] = 1
                   q.append((nx, ny))
count = 0
for a in range(n):
    for b in range(m):
        if board[a][b] == 0:
            count += 1
            bfs(board, a, b)

print(count)
    

