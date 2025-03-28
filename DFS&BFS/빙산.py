from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
def bfs(visited, ices, sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        non_ice = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    non_ice += 1
                elif not visited[nx][ny] and board[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
        ices.append((x, y, non_ice))
    
def probe_ice(board):
    visited = [[False] * m for _ in range(n)]
    count = 0
    ices = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] > 0:
                count += 1
                bfs(visited, ices, i, j)
    if not ices:
        return [-1]
    elif count >= 2:
        return [1]
    else:
        return ices

def remove_ice(ices):
    for ix, iy, reduce in ices:
        post_reduce = board[ix][iy] - reduce
        if post_reduce < 0:
            board[ix][iy] = 0
        else:
            board[ix][iy] = post_reduce

result = 0
while True:
    ices = probe_ice(board)
    
    if ices[0] == -1:
        result = 0
        break
    elif ices[0] == 1:
        break
    
    remove_ice(ices)
    result += 1

print(result)