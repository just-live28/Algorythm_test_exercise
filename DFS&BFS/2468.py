# 안전 영역이 최대 몇 개인가?
# 장마철 내리는 비의 양 이하 높이 모든 지점은 잠긴다
# Flood Fill
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = []
max_height = 0
for _ in range(n):
    line = list(map(int, input().split()))
    max_height = max(max_height, max(line))
    board.append(line)

def bfs(visited, i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > rain and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

max_safe_zone = 1
for rain in range(1, max_height):
    visited = [[False] * n for _ in range(n)]
    safe_zone = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > rain and not visited[i][j]:
                safe_zone += 1
                bfs(visited, i, j)
    max_safe_zone = max(max_safe_zone, safe_zone)

print(max_safe_zone)