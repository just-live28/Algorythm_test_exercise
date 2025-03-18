from collections import deque
from itertools import combinations
import copy

n = int(input())
board = []
teachers = []
spaces = []
for i in range(n):
    line = input().split()
    board.append(line)
    for j in range(n):
        if line[j] == 'X':
            spaces.append((i, j))
        elif line[j] == 'T':
            teachers.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_avoid(board, teachers):
    q = deque(teachers)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x, y
            while True:
                nx, ny = nx + dx[i], ny + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 'S':
                        return False
                    elif board[nx][ny] == 'O':
                        break
                else:
                    break
    return True

enable = False
for obstacles in combinations(spaces, 3):
    nboard = copy.deepcopy(board)
    for ox, oy in obstacles:
        nboard[ox][oy] = 'O'
    if is_avoid(nboard, teachers):
        enable = True
        break

if enable:
    print("YES")
else:
    print("NO")