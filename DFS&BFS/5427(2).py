from collections import deque
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    board = []
    hx, hy = 0, 0
    fires = []
    for i in range(h):
        line = list(input())
        board.append(line)
        for j in range(w):
            if line[j] == '@':
                hx, hy = i, j
            elif line[j] == '*':
                fires.append((i, j))
                
    fq = deque()
    f_visited = [[INF] * w for _ in range(h)]
    for fx, fy in fires:
        fq.append((0, fx, fy))
        f_visited[fx][fy] = 0
    
    while fq:
        count, x, y = fq.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '#' and count + 1 < f_visited[nx][ny]:
                f_visited[nx][ny] = count + 1
                fq.append((count + 1, nx, ny))

    hq = deque()
    hq.append((0, hx, hy))
    h_visited = [[-1] * w for _ in range(h)]
    h_visited[hx][hy] = 0
    result = INF
    while hq:
        count, x, y = hq.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                result = min(result, count + 1)
                break
            
            if board[nx][ny] == '.' and count + 1 < f_visited[nx][ny] and h_visited[nx][ny] == -1:
                h_visited[nx][ny] = count + 1
                hq.append((count + 1, nx, ny))

    if result == INF:
        print('IMPOSSIBLE')
    else:
        print(result)