from collections import deque

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        board[b][a] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx, ny))    

    count = 0
    for a in range(n):
        for b in range(m):
            if board[a][b] == 1:
                count += 1
                bfs(a, b)

    print(count)