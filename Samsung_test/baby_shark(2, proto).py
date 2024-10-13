import copy
from collections import deque
INF = int(1e9)

n = int(input())
ssize, sx, sy = 2, 0, 0

board= [[0]*(n+1) for _ in range(n+1)]
for a in range(1, n+1):
    line = list(map(int, input().split()))
    for b in range(1, n+1):
        if line[b-1] != 0:
            if line[b-1] != 9:
                board[a][b] = line[b-1]
            else:
                sx, sy = a, b

def find_fish():
    result = []
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            fsize = board[a][b]
        
            if fsize == 0 or ssize <= fsize:
                continue
        
            result.append((a, b))
        
    return result

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move_shark(board, tx, ty):
    board = copy.deepcopy(board)
    
    visited = [[False]*(n+1) for _ in range(n+1)]
    visited[sx][sy] = True
    
    q = deque()
    q.append((0, sx, sy))
    
    while q:
        l, x, y = q.popleft()
        
        if x == tx and y == ty:
            return l
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] <= ssize and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((l+1, nx, ny))
        
    return INF

t = 0
ate = 0
while True:
    targets = find_fish()
    
    result = []
    for fx, fy in targets:
        length = move_shark(board, fx, fy)
        
        if length != INF:
            result.append((length, fx, fy))
    
    if len(result) == 0:
        break
    
    result.sort()
    
    move_legnth, move_x, move_y = result[0]
    
    t += move_legnth
    board[move_x][move_y] = 0
    sx, sy = move_x, move_y
    ate += 1
    
    if ssize == ate:
        ate = 0
        ssize += 1

print(t)