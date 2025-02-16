from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
print(board)

visited = [[False] * m for _ in range(n)]
count = 0
max_length = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] or board[i][j] == 0:
            continue
        
        visited[i][j] = True
        q = deque()
        q.append((i, j))
        
        count += 1
        length = 0
        while q:
            x, y = q.popleft()
            length += 1
            
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
        max_length = max(max_length, length)

print(count)
print(max_length)