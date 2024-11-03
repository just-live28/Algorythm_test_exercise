# (time, 번호, x좌표, y좌표)
import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, k = map(int, input().split())

board = [[0]*(n+1) for _ in range(n+1)]

q = []
for a in range(1, n+1):
    line = list(map(int, input().split()))
    for b in range(1, n+1):
        if line[b-1] != 0:
            board[a][b] = line[b-1]
            heapq.heappush(q, (0, line[b-1], a, b))

s, x, y = map(int, input().split())

while q:
    t, vnum, vx, vy = heapq.heappop(q)
    
    if t == s:
        break
    
    for i in range(4):
        nx, ny = vx + dx[i], vy + dy[i]
        
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] == 0:
            board[nx][ny] = vnum
            heapq.heappush(q, (t+1, vnum, nx, ny))

print(board[x][y])