# N * N 격자 / 1~M 까지의 상어 / K 페로몬 유지 시간 / 작은 번호 상어가 가장 강력(같은 칸 도착 시 큰 상어 쫓아냄)

# board[a][b] = (상어 번호, 방향)
# peromon[a][b] = [상어 번호, 남은 유지시간]
# direction[shark] = [[4,4,3,1],[~~],[~~],[~~]]

# 1. 냄새 뿌리기
# 2. 동시에 모든 상어 상하좌우 중 하나로 이동 (우선순위 존재. 상어마다/방향마다) / 여러 상어 있을 시 작은 상어만 남음
#   상어 이동(모두 동시에 이동하므로, 딥카피 후 그것을 참고 삼아 이동 필요)
# 3. 1~2를 반복

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 도달할 수 없으면 board[a][b][0] = -1
board = [[(-1,-1)] * (n+1) for _ in range(n+1)]
# peromon[a][b][1] 이 0이면 페로몬이 없는 것
peromon = [[(0,0)] * (n+1) for _ in range(n+1)]
direction = [[] for _ in range(m+1)]

for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, n+1):
        board[i][j] = (line[j-1], 0)

init_direction = list(map(int, input().split()))

for i in range(1, m+1):
    direction[i].append(0)
    for _ in range(4):
        line = list(map(int, input().split()))
        direction[i].append(line)


def find_all_sharks_and_peromon_on():
    sharks = []
    for a in range(1, n+1):
        for b in range(1, n+1):
            snum, sdir = board[a][b]
            if snum > 0:
                sharks.append((a,b))
                peromon[a][b] = (snum, k)
    return sharks

def peromon_off():
    for a in range(1, n+1):
        for b in range(1, n+1):
            snum, sk = peromon[a][b]
            new_sk = sk - 1
            if new_sk <= 0:
                peromon[a][b] = (0, 0)
            else:
                peromon[a][b] = (snum, new_sk)
            
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

loop = False
result_time = 0
# 1번 상어가 3번 방향일 때 : direction[1][3]
while(True):
    # 이전 시간의 페로몬이 흩어짐.
    peromon_off()
    # 모든 상어의 위치를 찾고, 페로몬을 뿌림.
    sharks = find_all_sharks_and_peromon_on()
    if len(sharks) == 1:
        break
    
    # 초기 방향 설정
    if result_time == 0:
        for shark in sharks:
            sx ,sy = shark
            snum, sdir = board[sx][sy]
            board[sx][sy] = (snum, init_direction[snum-1])
    
    # 상어 이동
    for shark in sharks:
        sx, sy = shark
        snum, sdir = board[sx][sy]
        dir = direction[snum][sdir]
        # 페로몬이 없을 때 우선순위로 이동
        moved = False
        for i in dir:
            nx, ny = sx + dx[i], sy + dy[i]
            if 1 <= nx and nx <= n and 1 <= ny and ny <= n:
                if peromon[nx][ny][1] == 0:
                    moved = True
                    # 빈칸이면 이동 / 다른 상어의 번호가 크면 쫓아내고, 작다면 본인이 사라진다.
                    nnum, ndir = board[nx][ny]
                    if nnum == 0:
                        board[sx][sy], board[nx][ny] = (0,0), (snum, i)
                    else:
                        if snum < nnum:
                            board[sx][sy], board[nx][ny] = (0,0), (snum, i)
                        else:
                            board[sx][sy] = (0,0)
                    break         
        # 페로몬이 있을 때 우선순위로 이동
        if not moved:
            for i in dir:
                nx, ny = sx + dx[i], sy + dy[i]
                if 1 <= nx and nx <= n and 1 <= ny and ny <= n:
                    if peromon[nx][ny][0] == snum:
                        board[sx][sy], board[nx][ny] = (0,0), (snum, i)
                        break
    
    result_time += 1
    if result_time > 1000:
        loop = True
        break

if loop:
    print(-1)
else:
    print(result_time)