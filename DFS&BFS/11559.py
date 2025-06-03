from collections import deque

board = []
for _ in range(12):
    board.append([x for x in input()])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_combo(buyos, visited, bx, by):
    q = deque()
    q.append((bx, by))
    visited[bx][by] = True

    targets = [(bx, by)]
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < 12 and 0 <= ny < 6 and board[nx][ny] == board[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                targets.append((nx, ny))
                q.append((nx ,ny))

    if len(targets) >= 4:
        return True
    else:
        for tx, ty in targets:
            buyos[ty].append((tx, board[tx][ty]))
        return False

result = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    buyos = [[] for _ in range(6)]
    is_combo = False

    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                combo = check_combo(buyos, visited, i, j)
                if combo:
                    is_combo = True
    
    if is_combo:
        result += 1
        nboard = [['.'] * 6 for _ in range(12)]
        for j in range(6):
            num = 11
            buyos[j].sort(key = lambda x : (-x[0]))
            for i, color in buyos[j]:
                nboard[num][j] = color
                num -= 1
        board = nboard
    else:
        break

print(result)