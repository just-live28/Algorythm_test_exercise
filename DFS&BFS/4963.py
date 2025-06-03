from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def find_same_land(board, visited, lx, ly):
    q = deque()
    q.append((lx, ly))
    visited[lx][ly] = True

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

while True:
    w, h = map(int, input().split())

    if (w, h) == (0, 0):
        break

    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))

    count = 0
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and not visited[i][j]:
                count += 1
                find_same_land(board, visited, i, j)
    
    print(count)