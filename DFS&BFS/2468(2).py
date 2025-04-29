# flood fill
from collections import deque

max_result = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(visited, i, j, height):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
        
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
for h in range(1, 101):
    count = 0
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] > h and not visited[i][j]:
                count += 1
                bfs(visited, i, j, h)
    
    max_result = max(max_result, count)

print(max_result)