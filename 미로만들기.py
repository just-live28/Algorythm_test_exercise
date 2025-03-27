from collections import deque
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = []
distance = [[INF] * n for _ in range(n)]
for _ in range(n):
    board.append([int(x) for x in input()])

def dijkstra(sx, sy):
    distance[sx][sy] = 0
    q = deque()
    q.append((0, sx, sy))
    
    while q:
        dist, x, y = q.popleft()
        if dist > distance[x][y]:
            continue
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist
                if board[nx][ny] == 0:
                    cost += 1
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    q.append((cost, nx, ny))

dijkstra(0, 0)
print(distance[n-1][n-1])    