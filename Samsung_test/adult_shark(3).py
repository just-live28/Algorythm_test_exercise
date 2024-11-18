n, m, k = map(int, input().split())

board = []
sharks = [[-1,-1,-1] for _ in range(m+1)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] != 0:
            sharks[line[j]] = [i, j, 0]
    board.append(line)
sharks[0] = None

init_dir = list(map(int, input().split()))
for i in range(1, m+1):
    # 0~3 북 서 남 동
    sharks[i][2] = init_dir[i-1]

shark_directions = [[] for _ in range(m+1)]
for i in range(1, m+1):
    for _ in range(4):
        shark_directions[i].append(list(map(int, input().split())))

# (상어번호, 남은시간)
peromons = [[[0,0]]*n for _ in range(n)]

def diffuse_peromon(peromons, sharks):
    recent_positions = []
    for i in range(1, m+1):
        if sharks[i] != None:
            sx, sy, sdir = sharks[i]
            peromons[sx][sy] = [i, k]
            recent_positions.append((sx, sy))
    return recent_positions

def discount_peromon(peromons, recent_positions):
    for i in range(n):
        for j in range(n):
            if (i, j) not in recent_positions:
                peromons[i][j][1] -= 1
                
                if peromons[i][j][1] == 0:
                    peromons[i][j] = [0, 0]
                    
def count_sharks(sharks):
    count = 0
    for shark in sharks:
        if shark == None:
            continue
        count += 1
    return count          
                    
dir = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]
# board[x][y] = n // 0 빈칸 1> 상어 번호
# sharks[i] = [sx, sy, sdir] // None이면 없는 상어
# shark_directions[snum][sdir] = [n, n ,n ,n] //
# peromons[x][y] = [snum, k]
t = 0
diffuse_peromon(peromons, sharks)
while True:  
    if t > 1000:
        print(-1)
        break
    
    if count_sharks(sharks) == 1:
        print(t)
        break
    
    for i in range(m, 0, -1):
        if sharks[i] == None:
            continue
        
        sx, sy, sdir = sharks[i]
        
        moved = False
        for j in range(4):
            now_dir = shark_directions[i][sdir-1][j]
            nx, ny = sx + dir[now_dir][0], sy + dir[now_dir][1]
            
            if 0 <= nx < n and 0 <= ny < n and peromons[nx][ny][0] == 0:
                moved = True
                if board[nx][ny] != 0:
                    weak_snum = board[nx][ny]
                    sharks[weak_snum] = None
                
                board[sx][sy] = 0
                board[nx][ny] = i
                sharks[i] = [nx, ny, now_dir]
                break
        
        if not moved:
            for j in range(4):
                now_dir = shark_directions[i][sdir-1][j]
                nx, ny = sx + dir[now_dir][0], sy + dir[now_dir][1]

                if 0 <= nx < n and 0 <= ny < n and peromons[nx][ny][0] == i:
                    board[sx][sy] = 0
                    board[nx][ny] = i
                    sharks[i] = [nx, ny, now_dir]
                    break
    
    recent_positions = diffuse_peromon(peromons, sharks)
    discount_peromon(peromons, recent_positions)
    
    t += 1