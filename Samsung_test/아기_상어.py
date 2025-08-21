from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = []
sx, sy, size = 0, 0, 2
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(n):
        if line[j] == 9:
            sx, sy = i, j
            board[i][j] = 0

def find_eatable_fishes(sx, sy):
    q = deque()
    q.append((0, sx, sy))
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    
    candidates = []
    while q:
        dist, x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                
                if board[nx][ny] > size:
                    continue
                else:
                    q.append((dist+1, nx, ny))
                    
                    if board[nx][ny] > 0 and board[nx][ny] < size:
                        candidates.append((dist+1, nx, ny))
    
    return candidates

time = 0
ate = 0
while True:
    candidates = find_eatable_fishes(sx, sy)
    
    if not candidates:
        break
    elif len(candidates) > 1:
        candidates.sort(key = lambda x : (x[0], x[1], x[2]))
    
    dist, cx, cy = candidates[0]
    
    time += dist
    board[cx][cy] = 0
    sx, sy = cx, cy
    ate += 1
    
    if ate == size:
        size += 1
        ate = 0

print(time)