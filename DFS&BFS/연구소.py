# n * m 보드 / 0 빈칸 1 벽 2 바이러스
# 벽을 빈칸에 3개 세워서 바이러스 퍼뜨린 후, 남은 빈칸의 최대 개수
# 조합으로 빈 칸 중 3개를 선택 (deepcopy, combinations)

import copy
from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
origin_board = []
viruses = []
spaces = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 0:
            spaces.append((i, j))
        elif line[j] == 2:
            viruses.append((i, j))
    origin_board.append(line)

result = 0
for walls in combinations(spaces, 3):
    board = copy.deepcopy(origin_board)
    for wx, wy in walls:
        board[wx][wy] = 1
        
    q = deque(viruses)
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
    
    safe_zones = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                safe_zones += 1
    
    result = max(result, safe_zones)

print(result)