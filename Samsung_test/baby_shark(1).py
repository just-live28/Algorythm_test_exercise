import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
now_x, now_y = 0, 0
now_size = 2

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

for a in range(n):
    for b in range(n):
        if array[a][b] == 9:
            now_x, now_y = a, b
            array[a][b] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    dist = [[-1] * n for _ in range(n)]
    
    q = deque()
    q.append((now_x, now_y))
    dist[now_x][now_y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 지나가려면 자신 크기보다 같거나 작아야함.
            if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

def find_fish(dist):
    min_length = INF
    for i in range(n):
        for j in range(n):
            # 도달 가능한 칸에서, 자신보다 작은 크기의 물고기만 먹을 수 있음
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                if dist[i][j] < min_length:
                    min_length = dist[i][j]
                    x, y = i, j
    if min_length == INF:
        return None
    else:
        return min_length, x, y

time = 0
ate = 0

while(True):
    fish = find_fish(bfs())
    if fish == None:
        break
    length, fx, fy = fish
    time += length
    now_x, now_y = fx, fy
    array[fx][fy] = 0
    ate += 1
    
    if ate == now_size:
        now_size += 1
        ate = 0

print(time)