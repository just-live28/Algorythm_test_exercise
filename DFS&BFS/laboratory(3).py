import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())

spaces = []

origin_board = []
for a in range(n):
    line = list(map(int, input().split()))
    origin_board.append(line)
    for b in range(m):
        if line[b] == 0:
            spaces.append((a, b))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

max_result = 0
for walls in combinations(spaces, 3):
    board = copy.deepcopy(origin_board)
    
    for wx, wy in walls:
        board[wx][wy] = 1
    
    for a in range(n):
        for b in range(m):
            if board[a][b] == 2:
                q = deque()
                q.append((a, b))
                
                while q:
                    x, y = q.popleft()
                    
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        
                        if 0 <= nx < n and 0 <= ny < m:
                            if board[nx][ny] == 0:
                                board[nx][ny] = 2
                                q.append((nx, ny))
                                
    count = 0
    for a in range(n):
        for b in range(m):
            if board[a][b] == 0:
                count += 1
    
    if count > max_result:
        max_result = count

print(max_result)