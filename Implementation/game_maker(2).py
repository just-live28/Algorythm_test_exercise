
# 현재 방향 기준 왼쪽으로 회전
# 앞에 아직 가보지 않은 칸이 존재한다면 전진. / 가보지 않은 칸이 없다면 다시 회전
# 한바퀴를 다 돌았으면 뒤로 한칸 가고 다시 수행 / 이 때 뒤가 갈 수 없는 칸인 경우 종료


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 세로 n 가로 m
n, m = map(int, input().split())
x, y, dir = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

d = [[0] * m for _ in range(n)]

d[x][y] = 1
result = 1
while(True):
    moved = False
    for i in range(4):
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if board[nx][ny] == 0 and d[nx][ny] == 0:
                moved = True
                d[nx][ny] = 1
                x, y = nx, ny
                result += 1
                break
    if not moved:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if board[nx][ny] == 0:
                x, y = nx, ny
            else:
                break
print(result)
        
        