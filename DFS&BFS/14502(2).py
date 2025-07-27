import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
origin_board = []
spaces = []
viruses = []
for i in range(n):
    line = list(map(int, input().split()))
    origin_board.append(line)
    for j in range(m):
        if line[j] == 0:
            spaces.append((i, j))
        elif line[j] == 2:
            viruses.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_safe_zone(board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1

    return count

max_safe_zone = 0
for each in list(combinations(spaces, 3)):
    board = copy.deepcopy(origin_board)

    for sx, sy in each:
        board[sx][sy] = 1
    
    q = deque()
    visited = [[False] * m for _ in range(n)]

    for vx, vy in viruses:
        q.append((vx, vy))
        visited[vx][vy] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                board[nx][ny] = 2
                q.append((nx, ny))

    safe_zone = count_safe_zone(board)

    max_safe_zone = max(max_safe_zone, safe_zone)

print(max_safe_zone)