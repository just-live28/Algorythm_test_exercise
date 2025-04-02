# N * M 격자 / 0 빈칸 / 
# 산봉우리 : 같은 높이를 가지는 하나의 격자(+ 인접한 격자 : 더 작)
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def cal_mountain(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    height = board[x][y]
    
    is_top = True
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] > 0:
                nheight = board[nx][ny]
                if nheight > height:
                    is_top = False
                elif nheight == height and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
    return is_top

visited = [[False] * m for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] > 0 and not visited[i][j]:
            if cal_mountain(i, j):
                count += 1

print(count)