from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def add_targets(targets, visited, tx, ty):
    q = deque()
    q.append((tx, ty))

    while q:
        x, y = q.popleft()

        non_ice = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif board[nx][ny] == 0:
                    non_ice += 1
        targets.append((x, y, non_ice))

def decrease_ice(targets):
    for tx, ty, non_ice in targets:
        if board[tx][ty] - non_ice < 0:
            board[tx][ty] = 0
        else:
            board[tx][ty] = board[tx][ty] - non_ice

time = 0
while True:
    visited = [[False] * m for _ in range(n)]
    targets = []
    
    loaf = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                loaf += 1
                add_targets(targets, visited, i, j)
    
    if loaf == 0:
        print(0)
        break
    elif loaf > 1:
        print(time)
        break

    decrease_ice(targets)
    time += 1