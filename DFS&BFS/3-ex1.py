from collections import deque

n, m = map(int, input().split())

visited = [[False] * m for _ in range(n)]

board = [[0] * m for _ in range(n)]
for a in range(n):
    line = input()
    for b in range(m):
        board[a][b] = int(line[b])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def make_ice(a, b, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))

count = 0
for a in range(n):
    for b in range(m):
        if board[a][b] == 0 and visited[a][b] == False:
            count += 1
            make_ice(a, b, visited)

print(count)