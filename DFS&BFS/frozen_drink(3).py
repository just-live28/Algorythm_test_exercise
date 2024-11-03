from collections import deque

n, m = map(int, input().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

board = [[0]*m for _ in range(n)]
for a in range(n):
    line = input()
    for b in range(len(line)):
        board[a][b] = int(line[b])

count = 0
for a in range(n):
    for b in range(m):
        if board[a][b] == 0:
            count += 1
            
            q = deque()
            q.append((a,b))
            
            while q:
                x, y = q.popleft()
                
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    
                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == 0:
                            board[nx][ny] = 1
                            q.append((nx, ny))

print(count)
                            