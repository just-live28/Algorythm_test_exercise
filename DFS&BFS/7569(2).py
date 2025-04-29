from collections import deque
m, n, h = map(int, input().split())

dx = [-1 ,1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

board = []
non_mature = 0
matures = []
for k in range(h):
    box = []
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j] == 0:
                non_mature += 1
            elif line[j] == 1:
                matures.append((0, k, i, j))
        box.append(line)
    board.append(box)

result = -1
if matures and non_mature == 0:
    result = 0
else:
    q = deque(matures)
    
    while q:
        time, z, x, y = q.popleft()
        
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and board[nz][nx][ny] == 0:
                board[nz][nx][ny] = 1
                non_mature -= 1
                q.append((time + 1, nz, nx, ny))
                
        if non_mature == 0:
            result = time + 1
            break
            
print(result)