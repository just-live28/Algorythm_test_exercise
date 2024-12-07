from collections import deque

n, m = map(int, input().split())
board = [['O'] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

sx, sy = 0, 0
for i in range(n):
    line = input()
    for j in range(m):
        board[i][j] = line[j]
        if line[j] == 'I':
            sx, sy = i ,j

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append((sx, sy))
visited[sx][sy] = True

count = 0
while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'X' and visited[nx][ny] == False:
            visited[nx][ny] = True
            if board[nx][ny] == 'P':
                count += 1
            q.append((nx, ny))

if count == 0:
    print('TT')
else:
    print(count)