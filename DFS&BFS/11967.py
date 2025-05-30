from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = [[0] * (n+1) for _ in range(n+1)]
switches = [[[] for _ in range (n+1)] for _ in range(n+1)]
for _ in range(m):
    x, y, a, b = map(int, input().split())
    switches[x][y].append((a, b))
visited = set()

board[1][1] = 1
visited.add((1, 1))
q = deque()
q.append((1, 1))
candidates = set()
result = 1

while q:
    x, y = q.popleft()

    for sx, sy in switches[x][y]:
        if board[sx][sy] == 0:
            board[sx][sy] = 1
            result += 1
            candidates.add((sx, sy))
    
        for i in range(4):
            nx, ny = sx + dx[i], sy + dy[i]

            if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) in visited and (sx, sy) not in visited:
                visited.add((sx, sy))
                q.append((sx, sy))
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) in candidates and (nx, ny) not in visited:
            candidates.remove((nx, ny))
            visited.add((nx, ny))
            q.append((nx, ny))

print(result)