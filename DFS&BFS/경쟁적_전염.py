import heapq

n, k = map(int, input().split())
viruses = []
board = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(n):
        if line[j] > 0:
            viruses.append((line[j], i, j))
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []
for vnum, vx, vy in viruses:
    heapq.heappush(q, (0, vnum, vx, vy))

while q:
    time, vnum, vx, vy = heapq.heappop(q)
    
    if time == s:
        break
    
    for i in range(4):
        nx, ny = vx + dx[i], vy + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = vnum
            heapq.heappush(q, (time+1, vnum, nx, ny))

print(board[x-1][y-1])