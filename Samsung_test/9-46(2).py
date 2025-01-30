from collections import deque

n = int(input())

board = []
sx, sy, s_size = 0, 0, 2
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(n):
        if line[j] == 9:
            sx, sy = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_fishes(sx, sy):
    targets = []
    
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    
    q = deque()
    q.append((0, sx, sy))
    
    while q:
        dist, x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True
                if board[nx][ny] <= s_size:
                    q.append((dist + 1, nx, ny))
                    if 1 <= board[nx][ny] < s_size:
                        targets.append((dist + 1, nx, ny))
    return targets

ate = 0
time = 0
while True:
    targets = find_fishes(sx, sy)
    
    if len(targets) == 0:
        print(time)
        break
    
    if len(targets) > 1:
        targets.sort(key = lambda x : (x[0], x[1], x[2]))
    
    move_time, fx, fy = targets[0]
    
    board[sx][sy] = 0
    board[fx][fy] = 9
    sx, sy = fx, fy
    time += move_time
    ate += 1
    
    if ate == s_size:
        s_size += 1
        ate = 0