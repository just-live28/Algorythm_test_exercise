from collections import deque

n, l, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def make_union(unioned, ux, uy):
    q = deque()
    q.append((ux, uy))
    union = [(ux, uy)]
    total = board[ux][uy]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not unioned[nx][ny]:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    unioned[nx][ny] = True
                    union.append((nx, ny))
                    total += board[nx][ny]
                    q.append((nx, ny))
    
    return union, total

time = 0
while True:
    unioned = [[False] * n for _ in range(n)]
    moved = False
    for x in range(n):
        for y in range(n):
            if not unioned[x][y]:
                unioned[x][y] = True
                union, total = make_union(unioned, x, y)

                if len(union) > 1:
                    moved = True
                    per_people = total // len(union)
                    
                    for ux, uy in union:
                        board[ux][uy] = per_people

    if not moved:
        break
    time += 1
                
print(time)