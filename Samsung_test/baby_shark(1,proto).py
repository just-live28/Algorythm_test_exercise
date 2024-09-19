import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

board = [[0] * (n+1) for _ in range(n+1)]

fishs = []
for a in range(1, n+1):
    line = list(map(int, input().split()))
    for b in range(1, n+1):
        if line[b-1] != 0:
            if line[b-1] == 9:
                x, y = a, b
                board[a][b] = 0
            else:
                # fishs에 추가 (크기, x좌표, y좌표)
                fishs.append((line[b-1], a, b))
                board[a][b] = line[b-1]
fishs.sort()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
s = 2
eat = 0

def find_length(board, s, x, y):
    entire_length = [[-1] * (n+1) for _ in range(n+1)]
    q = deque()
    q.append((x, y))
    entire_length[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 1 or ny < 1 or nx > n or ny > n or board[nx][ny] > s or entire_length[nx][ny] != -1:
                continue
            else:
                entire_length[nx][ny] = entire_length[x][y] + 1
                q.append((nx, ny))
    return entire_length
    

def find_fish(board, fishs, s, x, y):
    target_fishs = []
    entire_length = find_length(board, s, x, y)
    for fish in fishs:
        scale, fx, fy = fish
        if scale >= s:
            break
        length = entire_length[fx][fy]
        target_fishs.append((length, fx, fy, scale, fx, fy))
    if len(target_fishs) == 0:
        return []
    else:
        target_fishs.sort(key = lambda x:(x[0], x[1], x[2]))
        return (target_fishs[0][0], target_fishs[0][3], target_fishs[0][4], target_fishs[0][5])

time = 0
while(True):
    target = find_fish(board, fishs, s, x, y)
    if len(target) == 0:
        break
    length, scale, fx, fy = target
    # 이동
    time += length
    x, y = fx, fy
    board[fx][fy] = 0
    eat += 1
    # 레벨업
    if eat == s:
        s += 1
        eat = 0
    fishs.remove((scale, fx, fy))

print(time)