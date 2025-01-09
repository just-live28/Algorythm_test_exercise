from collections import deque

n, m = map(int, input().split())

# 1-side인데 0side로 만들기

# 0 <= x < n    0 <= y < m
# n-1, m-1 일때 종료

board = []
for _ in range(n):
    board.append(list(map(int, input())))

visited = [[-1] * m for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

q = deque()
# (1,1) 은 0-side에서 (0,0)
q.append((0, 0))
visited[0][0] = 1
while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
            
print(visited[n-1][m-1])