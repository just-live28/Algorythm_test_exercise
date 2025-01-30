from collections import deque

n = int(input())

sx, sy = 0, 0
s_size = 2
board = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(n):
        if line[j] == 9:
            sx, sy = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_fishes():
    q = deque()
    q.append((0, sx, sy))
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    
    target_fishes = []
    while q:
        dist, x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True
                if board[nx][ny] > s_size:
                    continue
                else:
                    q.append((dist + 1, nx, ny))
                
                if 0 < board[nx][ny] < s_size:
                    target_fishes.append((dist + 1, nx, ny))
    return target_fishes
    
t = 0
eat_count = 0
while True:
    target_fishes = find_fishes()
    
    if len(target_fishes) == 0:
        break
    
    if len(target_fishes) > 1:
        target_fishes.sort(key = lambda x : (x[0], x[1], x[2]))
        
    f_dist, fx, fy = target_fishes[0] 
    
    t += f_dist
    board[sx][sy] = 0
    board[fx][fy] = 9
    sx, sy = fx, fy
    
    eat_count += 1
    if eat_count == s_size:
        s_size += 1
        eat_count = 0

print(t)