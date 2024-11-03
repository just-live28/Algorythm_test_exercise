from collections import deque

board=[[0,0,0,0,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]

# type) 0 가로 1 세로
# (time, x1, y1, x2, y2)

n = len(board)
nboard = [[1]*(n+2) for _ in range(n+2)]
for a in range(1, n+1):
    line = board[a-1]
    for b in range(1, len(line)+1):
        if line[b-1] == 0:
            nboard[a][b] = 0

visited = {(1,1,1,2): True}

q = deque()
q.append((0, 1, 1, 1, 2))

result = 0
while q:
    t, x1, y1, x2, y2 = q.popleft()
    
    if (x1 == n and y1 == n) or (x2 == n and y2 == n):
        result = t
        break
    
    if x1 == x2: #가로일 때
        if nboard[x1][y1-1] == 0 and (x1, y1-1, x1, y1) not in visited: #왼쪽이동
            visited[(x1, y1-1, x1, y1)] = True
            q.append((t+1, x1, y1-1, x1, y1))
        if nboard[x1][y2+1] == 0 and (x2, y2, x2, y2+1) not in visited: #오른쪽이동
            visited[(x2, y2, x2, y2+1)] = True
            q.append((t+1, x2, y2, x2, y2+1))
        if nboard[x1-1][y1] == 0 and nboard[x2-1][y2] == 0: #위쪽이 비었을 때
            if (x1-1, y1, x2-1, y2) not in visited: #위쪽 이동
                visited[(x1-1, y1, x2-1, y2)] = True
                q.append((t+1, x1-1, y1, x2-1, y2))
            if (x2-1, y2, x2, y2) not in visited: #시계방향 회전
                visited[(x2-1, y2, x2, y2)] = True
                q.append((t+1, x2-1, y2, x2, y2))
            if (x1-1, y1, x1, y1) not in visited: #반시계방향 회전
                visited[(x1-1, y1, x1, y1)] = True
                q.append((t+1, x1-1, y1, x1, y1))
        if nboard[x1+1][y1] == 0 and nboard[x2+1][y2] == 0: #아래쪽이 비었을 때
            if (x1+1, y1, x2+1, y2) not in visited: #아래쪽 이동
                visited[(x1+1, y1, x2+1, y2)] = True
                q.append((t+1, x1+1, y1, x2+1, y2))
            if (x1, y1, x1+1, y1) not in visited: #시계방향 회전
                visited[(x1, y1, x1+1, y1)] = True
                q.append((t+1, x1, y1, x1+1, y1))
            if (x2, y2, x2+1, y2) not in visited: #반시계방향 회전
                visited[(x2, y2, x2+1, y2)] = True
                q.append((t+1, x2, y2, x2+1, y2))
    elif y1 == y2: #세로일 때
        if nboard[x1-1][y1] == 0 and (x1-1,y1,x1,y1) not in visited: #위쪽 이동
            visited[(x1-1,y1,x1,y1)] = True
            q.append((t+1, x1-1,y1,x1,y1))
        if nboard[x2+1][y2] == 0 and (x2,y2,x2+1,y2) not in visited: #아래쪽 이동
            visited[(x2,y2,x2+1,y2)] = True
            q.append((t+1, x2,y2,x2+1,y2))
        if nboard[x1][y1-1] == 0 and nboard[x2][y2-1] == 0: #왼쪽이 비었을 때
            if (x1,y1-1,x2,y2-1) not in visited: #왼쪽 이동
                visited[(x1,y1-1,x2,y2-1)] = True
                q.append((t+1, x1,y1-1,x2,y2-1))
            if (x1,y1-1,x1,y1) not in visited: #시계방향 회전
                visited[(x1,y1-1,x1,y1)] = True
                q.append((t+1, x1,y1-1,x1,y1))
            if (x2,y2-1,x2,y2) not in visited: #반시계방향 회전
                visited[(x2,y2-1,x2,y2)] = True
                q.append((t+1, x2,y2-1,x2,y2))
        if nboard[x1][y1+1] == 0 and nboard[x2][y2+1] == 0: #아래쪽이 비었을 때
            if (x1,y1+1,x2,y2+1) not in visited: #아래쪽 이동
                visited[(x1,y1+1,x2,y2+1)] = True
                q.append((t+1, x1,y1+1,x2,y2+1))
            if (x2,y2,x2,y2+1) not in visited: #시계방향 회전
                visited[(x2,y2,x2,y2+1)] = True
                q.append((t+1, x2,y2,x2,y2+1))
            if (x1,y1,x1,y1+1) not in visited: #반시계방향 회전
                visited[(x1,y1,x1,y1+1)] = True
                q.append((t+1, x1,y1,x1,y1+1))

print(result)