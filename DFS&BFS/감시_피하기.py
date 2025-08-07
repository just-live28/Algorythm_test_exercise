import copy
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
origin_board = []
spaces = []
teachers = []
for i in range(n):
    line = input().split()
    origin_board.append(line)
    for j in range(n):
        if line[j] == 'X':
            spaces.append((i, j))
        elif line[j] == 'T':
            teachers.append((i, j))

def detect_student(board):
    for x, y in teachers:
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 'S':
                        return True
                    elif board[nx][ny] == 'O':
                        break
                else:
                    break
    return False

avoid = False
for obstacles in combinations(spaces, 3):
    board = copy.deepcopy(origin_board)

    for ox, oy in obstacles:
        board[ox][oy] = 'O'
    
    if not detect_student(board):
        avoid = True
        break

if avoid:
    print('YES')
else:
    print('NO')