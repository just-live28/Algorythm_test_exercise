from collections import deque

x, y, d = 1, 1, 0

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
directions = [[3, 2], [2, 3], [0, 1], [1, 0]]

n = int(input())
board = [[0] * (n+1) for _ in range(n+1)]

k = int(input())
for _ in range(k):
    ax, ay = map(int, input().split())
    board[ax][ay] = 1

l = int(input())
turns = deque()
for _ in range(l):
    turn_time, turn_dir = input().split()
    turns.append((int(turn_time), turn_dir))

tails = deque()
tails.append((0, 0))
time = 0
while True:
    time += 1
    x, y = x + dx[d], y + dy[d]
    
    if x <= 0 or x > n or y <= 0 or y > n or (x, y) in tails:
        break
    
    tails.append((x, y))
    if board[x][y] == 1:
        board[x][y] = 0
    else:
        tails.popleft()
    
    if turns and turns[0][0] == time:
        turn_time, turn_dir = turns.popleft()
        
        if turn_dir == 'L':
            d = directions[d][0]
        elif turn_dir == 'D':
            d = directions[d][1]

print(time)