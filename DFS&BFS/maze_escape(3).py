from collections import deque

n, m = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

board = [[0]*(m+2) for _ in range(n+2)]
for a in range(1, n+1):
    line = input()
    for b in range(1, m+1):
        board[a][b] = int(line[b-1])

q = deque()
q.append((1,1))

distance = [[-1]*(m+2) for _ in range(n+2)]
distance[1][1] = 1

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if board[nx][ny] == 1 and distance[nx][ny] == -1:
            distance[nx][ny] = distance[x][y] + 1
            q.append((nx, ny))

print(distance[n][m])
        