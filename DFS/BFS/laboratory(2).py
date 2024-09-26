# n x m 인 직사각형. 벽을 3개 세운다.
# 0 빈칸 1 벽 2 바이러스

# 중복 x, 순서 x -> 조합

# 0. 기존 board를 준비한다.
# 1. 벽을 세운다.
# 2. 퍼뜨린다
# 3. 개수를 센다
# 4. 최고기록을 넘어선다면 갱신한다.

import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())

board = [[-1] * m for _ in range(n)]

blanks = []
for a in range(n):
    line = list(map(int, input().split()))
    for b in range(m):
        if line[b] == 0:
            blanks.append((a, b))
        board[a][b] = line[b]

def spread(board, walls):
    nboard = copy.deepcopy(board)
    
    for x, y in walls:
        nboard[x][y] = 1
    
    
    for a in range(n):
        for b in range(m):
            if nboard[a][b] == 2:
                bfs(nboard, a, b)
    
    count = 0
    for a in range(n):
        for b in range(m):
            if nboard[a][b] == 0:
                count += 1
    
    return count

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board, a, b):
    q = deque()
    q.append((a, b))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx and nx < n and 0 <= ny and ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    q.append((nx, ny))

result = 0
for walls in list(combinations(blanks, 3)):
    safe_zones = spread(board, walls)
    result = max(result, safe_zones)

print(result)