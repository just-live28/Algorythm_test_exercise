from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())

board = [[-1] * (m+1) for _ in range(n+1)]
spaces = []
viruses = []
for a in range(1, n+1):
    line = list(map(int, input().split()))
    for b in range(1, m+1):
        board[a][b] = line[b-1]
        if line[b-1] == 0:
            spaces.append((a, b))
        elif line[b-1] == 2:
            viruses.append((a, b))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus_test(board, walls, viruses):
    nboard = copy.deepcopy(board)
    
    for wx, wy in walls:
        nboard[wx][wy] = 1
    
    q = deque()
    for vx, vy in viruses:
        q.append((vx, vy))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= m and nboard[nx][ny] == 0:
                nboard[nx][ny] = 2
                q.append((nx, ny))
    
    count = 0
    for a in range(1, n+1):
        for b in range(1, m+1):
            if nboard[a][b] == 0:
                count += 1
    
    return count

max_space = 0
for walls in combinations(spaces, 3):
    space = virus_test(board, walls, viruses)
    max_space = max(max_space, space)

print(max_space)        