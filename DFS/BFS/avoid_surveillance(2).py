# n * n 크기의 복도
# 선생님(T) / 학생(S) / 장애물(O) / 빈칸(X)
# 선생님 상하좌우로 그 방향의 모든 칸을 감시 / 단, 장애물에 가로막히면 볼수 없음.
# 빈 칸에서 3개의 장애물을 설치 (combinations)

import copy
from collections import deque
from itertools import combinations

n = int(input())

board = [['O'] * (n+1) for _ in range(n+1)]

spaces = []
teachers = []
for a in range(1, n+1):
    line = list(input().split())
    for b in range(1, n+1):
        if line[b-1] == 'X':
            spaces.append((a, b))
        elif line[b-1] == 'T':
            teachers.append((a, b))
        board[a][b] = line[b-1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(board, walls):
    nboard = copy.deepcopy(board)
    
    for wx, wy in walls:
        nboard[wx][wy] = 'O'
    
    q = deque(teachers)
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            for step in range(1, n):
                nx, ny = x + step * dx[i], y + step * dy[i]
                if 1 <= nx and nx <= n and 1 <= ny and ny <= n:
                    if nboard[nx][ny] == 'O':
                        break
                    if nboard[nx][ny] == 'S':
                      return True 
    return False

is_avoid = False            
for walls in list(combinations(spaces, 3)):
    if check(board, walls) == False:
        is_avoid = True
        break

if is_avoid:
    print("YES")
else:
    print("NO")