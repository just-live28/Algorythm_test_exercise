# 1 익토 0 안익토 -1 빈칸
# (z, x, y)
from collections import deque

dz = [-1,1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]

m, n, h = map(int, input().split())
board = [[] for _ in range(h)]
ripes = []
non_ripes = 0
for k in range(h):
    for i in range(n):
        line = list(map(int, input().split()))
        board[k].append(line)
        for j in range(m):
            if line[j] == 0:
                non_ripes += 1
            elif line[j] == 1:
                ripes.append((k, i, j, 0))

q = deque(ripes)
result = 0
while q:
    z, x, y, day = q.popleft()
    
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and board[nz][nx][ny] == 0:
            board[nz][nx][ny] = 1
            non_ripes -= 1
            if non_ripes == 0:
                result = day + 1
            q.append((nz, nx, ny, day+1))

if non_ripes != 0:
    print(-1)
else:
    print(result)