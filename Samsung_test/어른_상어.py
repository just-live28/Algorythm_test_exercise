# board (0-sided)
# sharks, dir (1-sided)
# n 보드 / m 상어 수

n, m, k = map(int, input().split())
board = []
sharks = [[-1, -1, -1] for _ in range(m+1)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] != 0:
            sharks[line[j]] = [-1, i, j]
cur_dir = list(map(int, input().split()))
for i in range(1, m+1):
    sharks[i][0] = cur_dir[i-1]

directions = [[] for _ in range(m+1)]
for i in range(1, m+1):
    directions[i].append(None)
    for _ in range(4):
        directions[i].append(list(map(int, input().split())))

peromons = [[[0, 0] for _ in range(n)] for _ in range(n)]
def diffuse_peromon(sharks, peromons):
    for snum in range(1, m+1):
        sd, sx, sy = sharks[snum]
        if sd == -1:
            continue

        peromons[sx][sy] = [snum, k]

dx = [None, -1, 1, 0, 0]
dy = [None, 0, 0, -1, 1]

def move_sharks(sharks):
    nboard = [[0] * n for _ in range(n)]

    for snum in range(1, m+1):
        sd, sx, sy = sharks[snum]
        if sd == -1:
            continue

        priority = directions[snum][sd]
        moved = False
        for i in priority:
            nx, ny = sx + dx[i], sy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and peromons[nx][ny][0] == 0:
                moved = True

                # 없는 경우
                if nboard[nx][ny] == 0:
                    sharks[snum] = [i, nx, ny]
                    nboard[nx][ny] = snum
                else:
                    # 더 강한 경우
                    if snum < nboard[nx][ny]:
                        sharks[nboard[nx][ny]][0] = -1
                        sharks[snum] = [i, nx, ny]
                        nboard[nx][ny] = snum
                    # 더 약한 경우
                    elif snum > nboard[nx][ny]:
                        sharks[snum][0] = -1
                break
        
        if not moved:
            for i in priority:
                nx, ny = sx + dx[i], sy + dy[i]

                if 0 <= nx < n and 0 <= ny < n and peromons[nx][ny][0] == snum:
                    sharks[snum] = [i, nx, ny]
                    nboard[nx][ny] = snum
                    break
    
    return nboard

def decrease_peromon(peromons):
    for i in range(n):
        for j in range(n):
            if peromons[i][j][1] > 0:
                peromons[i][j][1] -= 1

                if peromons[i][j][1] == 0:
                    peromons[i][j][0] = 0

def count_sharks(board):
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                count += 1

    return count

time = 0
while True:
    time += 1

    if time > 1000:
        time = -1
        break

    diffuse_peromon(sharks, peromons)
    board = move_sharks(sharks)

    if count_sharks(board) == 1:
        break

    decrease_peromon(peromons)

print(time)