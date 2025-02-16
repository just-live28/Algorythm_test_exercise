from collections import deque
import sys
input = sys.stdin.readline

# (h, n, m, 0)
m, n, h = map(int, input().split())
ripes = []
non_riped = 0
board = [[] for _ in range(h)]
for a in range(h):
    for b in range(n):
        line = list(map(int, input().split()))
        board[a].append(line)
        for c in range(m):
            if line[c] == 1:
                ripes.append((a, b, c, 0))
            elif line[c] == 0:
                non_riped += 1

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

q = deque(ripes)
time = 0
while q:
    z, x, y, t = q.popleft()
    
    if not q:
        time = t
    
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and board[nz][nx][ny] == 0:
            board[nz][nx][ny] = 1
            non_riped -= 1
            q.append((nz, nx, ny, t+1))

if non_riped > 0:
    print(-1)
else:
    print(time)