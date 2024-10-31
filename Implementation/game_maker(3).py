# n * m 보드
# 왼쪽 방향 부터
# 가보지 않은 칸 존재 시 전진 / 없다면 회전만 수행
# 4방향 모두 이동 못할 시 뒤로 1칸 / 뒤로 못간다면 종료

n, m = map(int, input().split())
x, y, d = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False]*(m+1) for _ in range(n+1)]

# 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def rotate(dir):
    return (dir + 1) % 4

result = 0

visited[x][y] = True
result += 1

while True:
    moved = False
    for _ in range(4):
        d = rotate(d)
        
        nx, ny = x + dx[d], y + dy[d]
        
        if board[nx][ny] == 0 and visited[nx][ny] == False:
            moved = True
            visited[nx][ny] = True
            result += 1
            x, y = nx, ny
    
    if not moved:
        nx, ny = x - dx[d], y - dy[d]
        
        if board[nx][ny] == 1:
            break
        else:
            x, y = nx, ny

print(result)
        
        
