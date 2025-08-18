from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
directions = [[2, 3], [3, 2], [1, 0], [0, 1]]

n = int(input())
# 0 빈 칸 / 1 벽 / 2 사과
board = [[1] * (n+2) for _ in range(n+2)]
for i in range(1, n+1):
    for j in range(1, n+1):
        board[i][j] = 0
k = int(input())
for _ in range(k):
    ax, ay = map(int, input().split())
    board[ax][ay] = 2
l = int(input())
turns = []
for _ in range(l):
    time, dir = input().split()
    turns.append((int(time), dir))

x, y = 1, 1
# 0 상 1 하 2 좌 3 우
dir = 3
turns_idx = 0
tails = deque()
tails.append((x, y))
time = 0
while True:
    time += 1
    
    nx, ny = x + dx[dir], y + dy[dir]
    if board[nx][ny] == 1 or (nx, ny) in tails:
        break
    
    if board[nx][ny] == 2:
        board[nx][ny] = 0
    else:
        tails.popleft()
    tails.append((nx, ny))
    x, y = nx, ny
    
    if turns_idx < l and turns[turns_idx][0] == time:
        if turns[turns_idx][1] == 'L':
            dir = directions[dir][0]
        else:
            dir = directions[dir][1]
        
        turns_idx += 1

print(time)