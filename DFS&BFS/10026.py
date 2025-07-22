from collections import deque
import copy

n = int(input())
normal_board = []
for _ in range(n):
    normal_board.append([x for x in input()])
blind_board = copy.deepcopy(normal_board)
for i in range(n):
    for j in range(n):
        if blind_board[i][j] == 'G':
            blind_board[i][j] = 'R'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board, visited, tx, ty):
    q = deque()
    q.append((tx, ty))
    visited[tx][ty] = True

    color = board[tx][ty]
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

normal_visited = [[False] * n for _ in range(n)]
blind_visited = [[False] * n for _ in range(n)]
normal_count = 0
blind_count = 0
for i in range(n):
    for j in range(n):
        if not normal_visited[i][j]:
            normal_count += 1
            bfs(normal_board, normal_visited, i, j)
        
        if not blind_visited[i][j]:
            blind_count += 1
            bfs(blind_board, blind_visited, i, j)

print(normal_count, blind_count)