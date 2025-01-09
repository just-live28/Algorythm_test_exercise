from itertools import combinations
import copy

n = int(input())
board = []
teachers = []
spaces = []
for a in range(n):
    line = list(input().split())
    board.append(line)
    for b in range(n):
        if line[b] == 'X':
            spaces.append((a, b))
        elif line[b] == 'T':
            teachers.append((a, b))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def find_student(board, teachers):
    for tx, ty in teachers:
        for i in range(4):
            step = 1
            while True:
                nx, ny = tx + dx[i] * step, ty + dy[i] * step
                
                if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 'O':
                    break
                
                if board[nx][ny] == 'S':
                    return True
                else:
                    step += 1
    return False
                
is_avoid = False
for obstacles in combinations(spaces, 3):
    nboard = copy.deepcopy(board)
    for ox, oy in obstacles:
        nboard[ox][oy] = 'O'
    
    if find_student(nboard, teachers) == False:
        is_avoid = True

if is_avoid:
    print("YES")
else:
    print("NO")