from itertools import 

board = []
for _ in range(5):
    board.append(input())
    
visited = [[False] * 5 for _ in range(5)]
result = [None] * 7
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def func(k, x, y):
    global count
    if k == 7:
        # 연결 확인 과정 추가 필요
        if result.count('S') >= 4:
            count += 1
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
            visited[nx][ny] = True
            result[k] = board[nx][ny]
            func(k+1, nx, ny)
            visited[nx][ny] = False

for i in range(5):
    for j in range(5):
        visited[i][j] = True
        result[0] = board[i][j]
        func(1, i, j)
        visited[i][j] = False

print(count)