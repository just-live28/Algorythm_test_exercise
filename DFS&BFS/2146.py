from collections import deque
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def mapping_idx(idx, tx, ty):
    board[tx][ty] = idx
    
    q = deque()
    q.append((tx, ty))
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                board[nx][ny] = idx
                q.append((nx, ny))

def cal_length(tx, ty):
    global result
    
    q = deque()
    q.append((0, tx, ty))
    visited = [[False] * n for _ in range(n)]
    visited[tx][ty] = True
    while q:
        dist, x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] > 0 and board[nx][ny] != board[tx][ty]:
                    result = min(result, dist)
                    return
                
                visited[nx][ny] = True
                q.append((dist + 1, nx, ny))
                
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]
idx = 1
for a in range(n):
    for b in range(n):
        if board[a][b] == 1 and not visited[a][b]:
            visited[a][b] = True
            mapping_idx(idx, a, b)
            idx += 1

result = INF
for a in range(n):
    for b in range(n):
        if board[a][b] > 0:
            cal_length(a, b)

print(result)