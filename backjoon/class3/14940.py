from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
tx, ty = 0, 0
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(m):
        if line[j] == 2:
            tx, ty= i, j
            board[i][j] = 0    

q = deque()
q.append((0, tx, ty))

visited = [[False] * m for _ in range(n)]
visited[tx][ty] = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    dist, x, y = q.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and board[nx][ny] == 1:
            visited[nx][ny] = True
            board[nx][ny] = dist + 1
            q.append((dist+1, nx, ny))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == False:
            print(-1, end=' ')
        else:
            print(board[i][j], end=' ')
    print()