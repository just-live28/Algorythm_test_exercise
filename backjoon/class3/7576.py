from collections import deque

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

board = []
completes = []
non_complets = 0
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(m):
        if line[j] == 1:
            completes.append((0, i, j))
        elif line[j] == 0:
            non_complets += 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque(completes)
time = 0
while q:
    t, x, y = q.popleft()
    
    if len(q) == 0:
        time = t
        
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
    
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            board[nx][ny] = 1
            non_complets -= 1
            
            q.append((t+1, nx, ny))
            
if non_complets == 0:
    print(time)
else:
    print(-1)