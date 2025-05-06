from collections import deque
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# h 행 w 열
# 탈출: .이면서, x좌표가 0 또는 h-1 / y좌표가 0 또는 w-1

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    board = []
    fires = []
    hx, hy = 0, 0
    for i in range(h):
        line = list(input())
        board.append(line)
        for j in range(w):
            if line[j] == '@':
                hx, hy = i, j
            elif line[j] == '*':
                fires.append((i, j))

    fire_visited = [[INF] * w for _ in range(h)]
    fq = deque()
    for fx, fy in fires:
        fire_visited[fx][fy] = 0
        fq.append((0, fx, fy))
    while fq:
        time, x, y = fq.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and (board[nx][ny] == '.' or board[nx][ny] == '@') and fire_visited[nx][ny] == INF:
                fire_visited[nx][ny] = time + 1
                fq.append((time+1, nx, ny))

    human_visited = [[-1] * w for _ in range(h)]
    hq = deque()
    hq.append((0, hx, hy))
    human_visited[hx][hy] = 0
    result = INF
    while hq:
        time, x, y = hq.popleft()
        if (board[x][y] == '.' or board[x][y] == '@') and (x == 0 or y == 0 or x == h-1 or y == w-1):
            result = min(result, time+1)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.' and time+1 < fire_visited[nx][ny] and human_visited[nx][ny] == -1:
                human_visited[nx][ny] = time + 1
                hq.append((time+1, nx, ny))

    if result == INF:
        print('IMPOSSIBLE')
    else:
        print(result)