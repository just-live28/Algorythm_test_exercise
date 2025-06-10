from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = []
do_x, do_y = 0, 0
for i in range(n):
    line = [x for x in input()]
    for j in range(m):
        if line[j] == 'I':
            do_x, do_y = i, j
    board.append(line)

# O 빈 공간 / X 벽 / I 도연(한 번) / P 사람
# 아무도 만나지 못하면 TT
visited = [[False] * m for _ in range(n)] 
visited[do_x][do_y] = True
q = deque()
q.append((do_x, do_y))
meet = 0
while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'X' and not visited[nx][ny]:
            visited[nx][ny] = True
            if board[nx][ny] == 'P':
                meet += 1
            q.append((nx, ny))

if meet:
    print(meet)
else:
    print("TT")