from collections import deque

r, c = map(int, input().split())
board = []
waters = []
sx, sy = 0, 0
home_x, home_y = 0, 0
for i in range(r):
    line = input()
    for j in range(c):
        if line[j] == '*':
            waters.append((i, j))
        elif line[j] == 'S':
            sx, sy = i, j
        elif line[j] == 'D':
            home_x, home_y = i, j
    board.append(line)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

water_q = deque(waters)
w_board = [[int(1e9)] * c for _ in range(r)]
for wx, wy in waters:
    w_board[wx][wy] = 0
while water_q:
    x, y = water_q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'X' and board[nx][ny] != 'D' and w_board[nx][ny] == int(1e9):
            w_board[nx][ny] = w_board[x][y] + 1
            water_q.append((nx, ny))
w_board[home_x][home_y] = int(1e9)

animal_q = deque()
animal_q.append((sx, sy))
a_board = [[-1] * c for _ in range(r)]
a_board[sx][sy] = 0
while animal_q:
    x, y = animal_q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'X' and a_board[nx][ny] == -1 and a_board[x][y] + 1 < w_board[nx][ny]:
            a_board[nx][ny] = a_board[x][y] + 1
            animal_q.append((nx, ny))

result = a_board[home_x][home_y]
if result == -1:
    print("KAKTUS")
else:
    print(result)