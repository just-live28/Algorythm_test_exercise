from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
non_riped = 0
ripes = []
board = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(m):
        if line[j] == 1:
            ripes.append((i, j, 0))
        elif line[j] == 0:
            non_riped += 1
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque(ripes)
time = 0
while q:
    x, y, t = q.popleft()
        
    if not q:
        time = t
        
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            board[nx][ny] = 1
            non_riped -= 1
            q.append((nx, ny, t+1))

if non_riped > 0:
    print(-1)
else:
    print(time)