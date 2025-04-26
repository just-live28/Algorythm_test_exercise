from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_candidate(board, sx, sy, s_size):
    candidate = []
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    
    q = deque()
    q.append((0, sx, sy))
    
    while q:
        l, x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and s_size >= board[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] > 0 and s_size > board[nx][ny]:
                    candidate.append((l + 1, nx, ny))
                q.append((l + 1, nx, ny))
        
    return candidate
    
n = int(input())
s_size, sx, sy = 2, 0, 0
board = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(n):
        if line[j] == 9:
            sx, sy = i, j
    
time = 0
eat_count = 0
while True:
    candidate = find_candidate(board, sx, sy, s_size)
    
    if not candidate:
        break
    
    if len(candidate) > 1:
        candidate.sort(key = lambda x : (x[0], x[1], x[2]))
        
    length, fx, fy = candidate[0]
        
    board[sx][sy] = 0
    board[fx][fy] = 9
    sx, sy = fx, fy
    
    time += length
    eat_count += 1
    
    if eat_count == s_size:
        s_size += 1
        eat_count = 0

print(time)