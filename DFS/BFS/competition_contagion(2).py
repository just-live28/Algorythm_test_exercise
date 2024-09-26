from collections import deque
import sys
input = sys.stdin.readline

# n * n 크기의 시험관 / 1~k 번의 바이러스
# 낮은 순서 바이러스부터 전이(상하좌우)
# s 초 후 x,y의 칸이 무엇인지 출력 (0 빈칸 1~k 바이러스)

n, k = map(int, input().split())

board = [[-1] * (n+2) for _ in range(n+2)]

# (t, v, x, y) 시간 / 바이러스 번호 / x좌표 / y좌표
# 낮은 번호의 바이러스부터 삽입해야 함. (큐 정렬 필요)
q = deque()

viruses = []
for a in range(1, n+1):
    line = list(map(int, input().split()))
    for b in range(1, n+1):
        if line[b-1] != 0:
            viruses.append((line[b-1], a, b))
        board[a][b] = line[b-1]
viruses.sort()

for virus in viruses:
    vnum, vx, vy = virus
    q.append((0, vnum, vx, vy))

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    if q[0][0] == s:
        break
    
    t, vnum, vx, vy = q.popleft()
    
    for i in range(4):
        nx, ny = vx + dx[i], vy + dy[i]
        
        if board[nx][ny] != -1 and board[nx][ny] == 0:
            board[nx][ny] = vnum
            q.append((t+1, vnum, nx, ny))

print(board[x][y])