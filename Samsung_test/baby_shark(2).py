# bfs : 각 칸의 최소 도달 거리를 체크 - 상어 크기보다 같거나 작은 칸만 이동 가능, -1인 경우 도달 불가한 칸
# find_fish(bfs()) : bfs를 체크해서 -1이 아닌 칸을 추려냄 / (거리, x, y)를 반환
# 거리만큼 t 추가 / board[x][y] = 0 / 상어 좌표 x, y로 이동 / ate +1 한 후, ate가 상어 사이즈와 같다면 초기화 후 상어 사이즈 +1
from collections import deque
INF = int(1e9)

n = int(input())

ssize = 2
sx, sy = 0, 0

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

for a in range(n):
    for b in range(n):
        if board[a][b] == 9:
            sx, sy = a, b
            board[a][b] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    dist = [[-1] * n for _ in range(n)]
    dist[sx][sy] = 0
    
    q = deque()
    q.append((sx, sy))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] <= ssize and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                
    return dist

def find_fish(dist):
    min_length = INF
    tx, ty = 0, 0
    for a in range(n):
        for b in range(n):
            # 물고기가 있으면서(0이 아니고) 상어보다 작아야 함 & 도달 가능해야 함
            if 1 <= board[a][b] < ssize and dist[a][b] != -1:
                if dist[a][b] < min_length:
                    min_length = dist[a][b]
                    tx, ty = a, b
    
    if min_length == INF:
        return None
    else:
        return min_length, tx, ty

ate = 0
t = 0
while True:
    target = find_fish(bfs())
    
    if target == None:
        print(t)
        break
    
    t += target[0]
    board[target[1]][target[2]] = 0
    sx, sy = target[1], target[2]
    ate += 1
    
    if ate == ssize:
        ate = 0
        ssize += 1