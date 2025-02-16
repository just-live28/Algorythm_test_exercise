from collections import deque

r, c = map(int, input().split())
board = []
fires = []
jx, jy = 0, 0
for a in range(r):
    line = [x for x in input()]
    board.append(line)
    for b in range(c):
        if line[b] == 'J':
            jx, jy = a, b
        elif line[b] == 'F':
            fires.append((a, b))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

fq = deque(fires)
f_dist = [[-1] * c for _ in range(r)]
for a, b in fires:
    f_dist[a][b] = 0
while fq:
    x, y = fq.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != '#' and f_dist[nx][ny] == -1:
            f_dist[nx][ny] = f_dist[x][y] + 1
            fq.append((nx, ny))

jq = deque()
jq.append((jx, jy, 0))
j_dist = [[-1] * c for _ in range(r)]
j_dist[jx][jy] = 0
is_possible = -1
while jq:
    x, y, t = jq.popleft()
    
    if (x == 0 or x == r-1 or y == 0 or y == c-1) and (f_dist[x][y] == -1 or t < f_dist[x][y]):
        is_possible = t
        break
        
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != '#' and j_dist[nx][ny] == -1 and (f_dist[nx][ny] == -1 or t+1 < f_dist[nx][ny]):
            j_dist[nx][ny] = t+1
            jq.append((nx, ny, t+1))

if is_possible == -1:
    print('IMPOSSIBLE')
else:
    print(is_possible+1)