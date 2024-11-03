from collections import deque

# (1, 1)은 board[0][0]
board = [[0,0,0,1,1], [0,0,0,1,0], [0,1,0,1,1], [1,1,0,0,1], [0,0,0,0,0]]
n = 5

x1, y1, x2, y2 = 1, 1, 1, 2

# (a1, b1, a2, b2)
visited = set()
visited.add((x1, y1, x2, y2))

# (t, a1, b1, a2, b2)
q = deque()
q.append((0, x1, y1, x2, y2))

answer = 0
while q:
    t, x1, y1, x2, y2 = q.popleft()
    
    if (x1 == n and y1 == n) or (x2 == n and y2 == n):
        answer = t
        break
    
    dx, dy = x2 - x1, y2 - y1
    
    #앞쪽 이동이 가능한 경우
    nx, ny = x2 + dx, y2 + dy
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx-1][ny-1] == 0:
        if (x2, y2, nx, ny) not in visited:
            visited.add((x2, y2, nx, ny))
            q.append((t+1, x2, y2, nx, ny))
    #뒤쪽 이동이 가능한 경우
    nx, ny = x1 - dx, y1 - dy
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx-1][ny-1] == 0:
        if (nx, ny, x1, y1) not in visited:
            visited.add((nx, ny, x1, y1))
            q.append((t+1, nx, ny, x1, y1))
    #왼쪽 이동 / 왼편으로 회전이 가능한 경우
    if dy != 0:
        lnx, lny = x1 - dy, y1
        rnx, rny = x2 - dy, y2
    elif dx != 0:
        lnx, lny = x1, y1 - dx
        rnx, rny = x2, y2 - dx
                 
    if 1 <= lnx <= n and 1 <= lny <= n and 1 <= rnx <= n and 1 <= rny <= n and board[lnx-1][lny-1] == 0 and board[rnx-1][rny-1] == 0:
        if (lnx, lny, rnx, rny) not in visited:
            visited.add((lnx, lny, rnx, rny))
            q.append((t+1, lnx, lny, rnx, rny))
        if (rnx, rny, x2, y2) not in visited:
            visited.add((rnx, rny, x2, y2))
            q.append((t+1, rnx, rny, x2, y2))
        if (lnx, lny, x1, y1) not in visited:
            visited.add((lnx, lny, x1, y1))
            q.append((t+1, lnx, lny, x1, y1))
    #오른쪽 이동 / 오른편으로 회전이 가능한 경우
    if dy != 0:
        lnx, lny = x1 + dy, y1
        rnx, rny = x2 + dy, y2
    elif dx != 0:
        lnx, lny = x1, y1 + dx
        rnx, rny = x2, y2 + dx
                       
    if 1 <= lnx <= n and 1 <= lny <= n and 1 <= rnx <= n and 1 <= rny <= n and board[lnx-1][lny-1] == 0 and board[rnx-1][rny-1] == 0:
        if (lnx, lny, rnx, rny) not in visited:
            visited.add((lnx, lny, rnx, rny))
            q.append((t+1, lnx, lny, rnx, rny))
        if (x1, y1, lnx, lny) not in visited:
            visited.add((x1, y1, lnx, lny))
            q.append((t+1, x1, y1, lnx, lny))
        if (x2, y2, rnx, rny) not in visited:
            visited.add((x2, y2, rnx, rny))
            q.append((t+1, x2, y2, rnx, rny))
            
print(answer)