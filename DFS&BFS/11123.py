from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    board = []
    for _ in range(h):
        board.append(input())

    def bfs(visited, tx, ty):
        q = deque()
        q.append((tx, ty))
        visited[tx][ty] = True

        while q:
            x, y = q.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and board[nx][ny] == '#':
                    visited[nx][ny] = True
                    q.append((nx, ny))

    visited = [[False] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == '#' and not visited[i][j]:
                count += 1
                bfs(visited, i, j)

    print(count)