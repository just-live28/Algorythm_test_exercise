# W 흰색 / B 파란색
# 모일수록 강해진다 - N명이 뭉치면 N제곱의 위력
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(m):
    board.append(input())

w_power = 0
b_power = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_power(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    color = board[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == color and not visited[nx][ny]:
                count += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    
    return count ** 2

visited = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            power = get_power(i, j)
            if board[i][j] == 'W':
                w_power += power
            else:
                b_power += power

print(w_power, b_power)