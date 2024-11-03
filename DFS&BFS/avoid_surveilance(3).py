import copy
from itertools import combinations

n = int(input())

origin_board = []

spaces = []
teachers = []
for a in range(n):
    line = list(input().split())
    for b in range(n):
        if line[b] == 'X':
            spaces.append((a, b))
        elif line[b] == 'T':
            teachers.append((a, b))
    origin_board.append(line)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def avoid_teacher(board):
    for tx, ty in teachers:
        for i in range(4):
            for step in range(1, n):
                nx, ny = tx + step * dx[i], ty + step * dy[i]
                
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 'O':
                        break
                    elif board[nx][ny] == 'S':
                        return False
    
    return True

is_avoid = False
for obstacles in combinations(spaces, 3):
    nboard = copy.deepcopy(origin_board)
    
    for ox, oy in obstacles:
        nboard[ox][oy] = 'O'
    
    if avoid_teacher(nboard) == True:
        is_avoid = True
        break

if is_avoid:
    print("YES")
else:
    print("NO")