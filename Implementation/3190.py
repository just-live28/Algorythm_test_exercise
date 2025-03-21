# 사과가 1-sided 하게 주어진다.
from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
l = int(input())
turns = deque()
for _ in range(l):
    a, b = input().split()
    turns.append((int(a), b))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, dir, time = 0, 0, 0, 0
tails = deque()
tails.append((0, 0))
time = 0
while True:
    time += 1
    nx, ny = x + dx[dir], y + dy[dir]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in tails:
        break
    
    tails.append((nx, ny))
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        if tails:
            tails.popleft()
    
    if turns and time == turns[0][0]:
        _, move = turns.popleft()
        if move == 'L':
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
    x, y = nx, ny

print(time)    