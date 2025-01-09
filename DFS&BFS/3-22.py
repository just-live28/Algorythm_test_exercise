# dic = {}
# dic[(1,1)] = True
# print((1,2) in dic)
from collections import deque

board = [[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]

n = len(board)
nboard = []
nboard.append([1] * (n+2))
for i in range(n):
    line = [1]
    line.extend(board[i])
    line.append(1)
    nboard.append(line)
nboard.append([1] * (n+2))

history = {}
history[(1,1,1,2)] = 1

q = deque()
# x1, y1, x2, y2, t
q.append((1, 1, 1, 2, 0))

result = 0
while q:
    x1, y1, x2, y2, t = q.popleft()
    
    if (x1 == n and y1 == n) or (x2 == n and y2 == n):
        result = t
    
    # 가로로 놓여져 있을 때
    if x1 == x2:
        if nboard[x1][y1-1] == 0 and (x1, y1-1, x1, y1) not in history:
            history[(x1, y1-1, x1, y1)] = 1
            q.append((x1, y1-1, x1, y1, t+1))
        if nboard[x1][y2+1] == 0 and (x2, y2, x2, y2+1) not in history:
            history[(x2, y2, x2, y2+1)] = 1
            q.append((x2, y2, x2, y2+1, t+1))
        if nboard[x1-1][y1] == 0 and nboard[x1-1][y2] == 0:
            if (x1-1, y1, x1-1, y2) not in history:
                history[(x1-1, y1, x1-1, y2)] = 1
                q.append((x1-1, y1, x1-1, y2, t+1))
            if (x1-1, y1, x1, y1) not in history:
                history[(x1-1, y1, x1, y1)] = 1
                q.append((x1-1, y1, x1, y1, t+1))
            if (x1-1, y2, x2, y2) not in history:
                history[(x1-1, y2, x2, y2)] = 1
                q.append((x1-1, y2, x2, y2, t+1))
        if nboard[x1+1][y1] == 0 and nboard[x1+1][y2] == 0:
            if (x1+1, y1, x1+1, y2) not in history:
                history[(x1+1, y1, x1+1, y2)] = 1
                q.append((x1+1, y1, x1+1, y2, t+1))
            if (x1, y1, x1+1, y1) not in history:
                history[(x1, y1, x1+1, y1)] = 1
                q.append((x1, y1, x1+1, y1, t+1))
            if (x2, y2, x1+1, y2) not in history:
                history[(x2, y2, x1+1, y2)] = 1
                q.append((x2, y2, x1+1, y2, t+1))
    # 세로로 놓여져 있을 때
    if y1 == y2:
        if nboard[x1-1][y1] == 0 and (x1-1, y1, x1, y1) not in history:
            history[(x1-1, y1, x1, y1)] = 1
            q.append((x1-1, y1, x1, y1, t+1))
        if nboard[x2+1][y1] == 0 and (x2, y2, x2+1, y1) not in history:
            history[(x2, y2, x2+1, y1)] = 1
            q.append((x2, y2, x2+1, y1, t+1))
        if nboard[x1][y1-1] == 0 and nboard[x2][y1-1] == 0:
            if (x1, y1-1, x2, y1-1) not in history:
                history[(x1, y1-1, x2, y1-1)] = 1
                q.append((x1, y1-1, x2, y1-1, t+1))
            if (x1, y1-1, x1, y1) not in history:
                history[(x1, y1-1, x1, y1)] = 1
                q.append((x1, y1-1, x1, y1, t+1))
            if (x2, y1-1, x2, y2) not in history:
                history[(x2, y1-1, x2, y2)] = 1
                q.append((x2, y1-1, x2, y2, t+1))
        if nboard[x1][y1+1] == 0 and nboard[x2][y1+1] == 0:
            if (x1, y1+1, x2, y1+1) not in history:
                history[(x1, y1+1, x2, y1+1)] = 1
                q.append((x1, y1+1, x2, y1+1, t+1))
            if (x1, y1, x1, y1+1) not in history:
                history[(x1, y1, x1, y1+1)] = 1
                q.append((x1, y1, x1, y1+1, t+1))
            if (x2, y2, x2, y1+1) not in history:
                history[(x2, y2, x2, y1+1)] = 1
                q.append((x2, y2, x2, y1+1, t+1))
                
print(result)