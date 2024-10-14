n, m, k = map(int, input().split())

board = [[0]*(n+1) for _ in range(n+1)]
# 다른 객체로 처리하기 위해서는 * 가 아닌 큰 list 안에서 for 문을 써줘야 함.
sharks = [[-1, -1, -1] for _ in range(m+1)]
peromon = [[[0, 0]]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    line = list(map(int, input().split()))
    for b in range(1, n+1):
        if line[b-1] != 0:
            board[a][b] = line[b-1]
            sharks[line[b-1]] = [-1, a, b]

init_directions = list(map(int, input().split()))
for i in range(1, m+1):
    sharks[i][0] = init_directions[i-1]

sdir = [[()] for _ in range(m+1)]

for i in range(1, m+1):
    for _ in range(4):
        sdir[i].append(list(map(int, input().split())))

dir = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]

def move_shark():
    count = 0
    for i in range(1, m+1):
        if sharks[i][0] == -1:
            continue
        
        count += 1
        now_dir, now_x, now_y = sharks[i]
        
        moved = False
        for d in sdir[i][now_dir]:
            nx, ny = now_x + dir[d][0], now_y + dir[d][1]
            
            if 1 <= nx <= n and 1 <= ny <= n and peromon[nx][ny][0] == 0:
                moved = True
                if board[nx][ny] == 0:
                    board[nx][ny] = i
                    board[now_x][now_y] = 0
                    sharks[i] = [d, nx, ny]
                else:
                    if board[nx][ny] < i:
                        board[now_x][now_y] = 0
                        sharks[i] = [-1, -1, -1]
                    else:
                        sharks[board[nx][ny]] = [-1, -1, -1]
                        sharks[i] = [d, nx, ny]
                        board[nx][ny] = i
                        board[now_x][now_y] = 0
                break
        
        if not moved:
            for d in sdir[i][now_dir]:
                nx, ny = now_x + dir[d][0], now_y + dir[d][1]
                
                if 1 <= nx <= n and 1 <= ny <= n and peromon[nx][ny][0] == i:
                    board[nx][ny] = i
                    board[now_x][now_y] = 0
                    sharks[i] = [d, nx, ny]
                    #움직였을 때에 break
                    break
                
    return count

def spray_peromon():
    for i in range(1, m+1):
        if sharks[i][0] == -1:
            continue
        
        now_x, now_y = sharks[i][1], sharks[i][2]
        
        peromon[now_x][now_y] = [i, k]

def decrease_peromon():
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 페로몬이 남아있으면서, 그 칸에 상어가 없는 칸 = 상어가 페로몬을 남겼던 칸
            if peromon[a][b][0] != 0 and board[a][b] == 0:
                peromon[a][b][1] -= 1
                
                if peromon[a][b][1] == 0:
                    peromon[a][b][0] = 0

t = 0
loop = False
#초기 위치에 각 상어가 페로몬을 뿌림
spray_peromon()
while True:
    # 1000초가 넘는다면 종료
    if t > 1000:
        loop = True
        break
    
    #1. 상어 이동
    count = move_shark()
    
    if count == 1:
        break
    
    #2. 페로몬 뿌리기
    spray_peromon()
    #3. 이전 페로몬들 감소
    decrease_peromon()
    
    t += 1

if loop:
    print(-1)
else:
    print(t)