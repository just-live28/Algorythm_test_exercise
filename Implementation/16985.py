# 5 * 5 * 5판 / 0 벽 1 빈칸
# 각각의 판을 임의로 배치할 수 있음. -> 순열
# 각 판을 "회전" 가능 -> 4 * 4 * 4 * 4 * 4 가지
# 각 경우의 수마다 맨 윗 판 꼭짓점 중 하나 시작(큐) -> 상, 하, 좌, 우, 위, 아래 로 이동
# 큐가 끝나고 나서, 맨 아랫판의 입구 대각선 꼭짓점 횟수를 result에 갱신 시도

from collections import deque
from itertools import permutations
INF = int(1e9)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

orders = [0, 1, 2, 3, 4]
pairs = [[(0, 0, 0), (4, 4, 4)], [(0, 4, 0), (4, 0, 4)], [(4, 0, 0), (0, 4, 4)], [(4, 4, 0), (0, 0, 4)]]

# dir / floor / x / y
origin_board = [[[[0] * 5 for _ in range(5)] for _ in range(5)] for _ in range(4)]
for i in range(5):
    for j in range(5):
        line = list(map(int, input().split()))
        for k in range(5):
            origin_board[0][i][j][k] = line[k]
    
    for j in range(5):
        for k in range(5):
            origin_board[1][i][j][k] = origin_board[0][i][4-k][j]
    for j in range(5):
        for k in range(5):
            origin_board[2][i][j][k] = origin_board[1][i][4-k][j]
    for j in range(5):
        for k in range(5):
            origin_board[3][i][j][k] = origin_board[2][i][4-k][j]

result = INF
done = False
board = [[[0] * 5 for _ in range(5)] for _ in range(5)]
for f1, f2, f3, f4, f5 in permutations(orders, 5):
    if done:
        break
    
    for a in range(4):
        board[0] = origin_board[a][f1]
        for b in range(4):
            board[1] = origin_board[b][f2]
            for c in range(4):
                board[2] = origin_board[c][f3]
                for d in range(4):
                    board[3] = origin_board[d][f4]
                    for e in range(4):
                        board[4] = origin_board[e][f5]
                        
                        for st, en in pairs:
                            if board[st[0]][st[1]][st[2]] == 0 or board[en[0]][en[1]][en[2]] == 0:
                                continue
                            
                            visited = [[[INF] * 5 for _ in range(5)] for _ in range(5)]
                            visited[st[0]][st[1]][st[2]] = 0
                            q = deque()
                            q.append((st[0], st[1], st[2], 0))
                            
                            while q:
                                x, y, z, count = q.popleft()
                                
                                for i in range(6):
                                    nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                                    
                                    if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and board[nx][ny][nz] == 1 and visited[nx][ny][nz] == INF:
                                        visited[nx][ny][nz] = count + 1
                                        q.append((nx, ny, nz, count + 1))
                            
                            result = min(result, visited[en[0]][en[1]][en[2]])
                            if result == 12:
                                done = True

if result == INF:
    print(-1)
else:
    print(result)