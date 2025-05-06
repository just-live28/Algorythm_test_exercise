from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_externals(board):
    externals = set()
    externals.add((0, 0))
    eq = deque()
    eq.append((0, 0))
    external_visited = [[False] * m for _ in range(n)]
    external_visited[0][0] = True
    while eq:
        x, y = eq.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and not external_visited[nx][ny]:
                external_visited[nx][ny] = True
                externals.add((nx, ny))
                eq.append((nx, ny))
    
    return externals

def find_melting_cheeses(tx, ty, externals, visited, targets):
    q = deque()
    q.append((tx, ty))
    visited[tx][ty] = True
    
    while q:
        x, y = q.popleft()
        
        count = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif board[nx][ny] == 0 and (nx ,ny) in externals:
                    count += 1
        
        if count >= 2:
            targets.add((x, y))

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

time = 0
while True:
    externals = find_externals(board)
    
    visited = [[False] * m for _ in range(n)]
    melts = set()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                find_melting_cheeses(i, j, externals, visited, melts)
    
    if not melts:
        break
    
    for mx, my in melts:
        board[mx][my] = 0
    
    time += 1

print(time)