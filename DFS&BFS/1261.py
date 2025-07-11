from collections import deque
INF = int(1e9)

m, n = map(int, input().split())
board = []
for _ in range(n):
    board.append([int(x) for x in input()])

visited = [[INF] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
# count, x, y
q.append((0, 0, 0))
result = INF
while q:
    count, x, y = q.popleft()

    if (x, y) == (n-1, m-1):
        result = min(result, count)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and count < visited[nx][ny]:
            visited[nx][ny] = count
            
            if board[nx][ny] == 0:
                q.append((count, nx, ny))
            else:
                q.append((count + 1, nx, ny))

print(result)