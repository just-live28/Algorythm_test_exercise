from collections import deque

n = int(input())
k = int(input())
apples= []
for _ in range(k):
    ax, ay = map(int, input().split())
    apples.append((ax, ay))

board = [[0]*(n+1) for _ in range(n+1)]

x, y, d = 1, 1, 0

body = deque()
body.append((1,1))

#동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

directions = [(3, 1), (0, 2), (1, 3), (2, 0)]

for ax, ay in apples:
    board[ax][ay] = 1

l = int(input())

q = deque()
for _ in range(l):
    time, dir = input().split()
    q.append((int(time), dir))

t = 0
while True:
    t += 1
    nx, ny = x + dx[d], y + dy[d]
    
    if 1 <= nx <= n and 1 <= ny <= n:
        if (nx, ny) in body:
            break
        
        body.append((nx, ny))
        
        if board[nx][ny] == 1:
            board[nx][ny] = 0
        else:
            body.popleft()
        
        x, y = nx, ny
             
        if q and q[0][0] == t:
            time, dir = q.popleft()

            if dir == 'L':
                d = directions[d][0]
            elif dir == 'D':
                d = directions[d][1]
    else:
        break

print(t)