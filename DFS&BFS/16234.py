from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))


def find_union(visited):
    visited[i][j] = True
    q = deque()
    q.append((i, j))
    union = [(i, j)]
    total = board[i][j]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    total += board[nx][ny]
                    q.append((nx, ny))
    return union, total

day = 0
while True:
    visited = [[False] * n for _ in range(n)]
    moved = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union, total = find_union(visited)
                if len(union) > 1:
                    moved = True
                    each = total // len(union)
                    for ux, uy in union:
                        board[ux][uy] = each
    if not moved:
        break
    else:
        day += 1

print(day)