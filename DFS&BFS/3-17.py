from collections import deque

# n*n 보드 k개의 바이러스
n, k = map(int, input().split())
board = []
viruses = []
for a in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for b in range(n):
        if line[b] != 0:
            viruses.append((line[b], a, b))

s, x, y = map(int, input().split())

viruses.sort()
q = deque()
for vi, vx, vy in viruses:
    q.append((vi, 0, vx, vy))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    vi, vt, vx, vy = q.popleft()
    
    if vt == s:
        break
    
    for i in range(4):
        nx, ny = vx + dx[i], vy + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = vi
            q.append((vi, vt+1, nx, ny))

print(board[x-1][y-1])