from collections import deque
from itertools import combinations
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def put_walls(board, walls):
    for wx, wy, in walls:
        board[wx][wy] = 1

def diffuse_viruses(board, viruses):
    q = deque()
    for vx, vy in viruses:
        q.append((vx, vy))    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))

def count_safe_zone(board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1
    return count

n, m = map(int, input().split())
spaces = []
viruses = []
max_safe_zone = 0
board = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(m):
        if line[j] == 0:
            spaces.append((i, j))
        elif line[j] == 2:
            viruses.append((i, j))

for walls in combinations(spaces, 3):
    nboard = copy.deepcopy(board)
    put_walls(nboard, walls)
    diffuse_viruses(nboard, viruses)
    safe_zone = count_safe_zone(nboard)
    max_safe_zone = max(max_safe_zone, safe_zone)

print(max_safe_zone)