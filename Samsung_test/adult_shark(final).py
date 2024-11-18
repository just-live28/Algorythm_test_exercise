# n 맵 크기 / m 상어 수 / k 페로몬 지속시간
n, m, k = map(int, input().split())

board = [[0]*(n+1) for _ in range(n+1)]
sharks = [None for _ in range(m+1)]
for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, n+1):
        if line[j-1] != 0:
            sharks[line[j-1]] = [i, j, 0]
            board[i][j] = line[j-1]

shark_directions = [[] for _ in range(m+1)]
peromons = [[[0,0]] * (n+1) for _ in range(n+1)]

init_dir = list(map(int, input().split()))
for i in range(1, m+1):
    sharks[i][2] = init_dir[i-1]

for i in range(1, m+1):
    shark_directions[i].append([0])
    for _ in range(4):
        shark_directions[i].append(list(map(int, input().split())))

dir = [(0,0), (-1,0),(1,0),(0,-1),(0,1)]

def diffuse_peromon(peromons, sharks):
    for i in range(1, m+1):
        if sharks[i] == None:
            continue
        sx, sy, sdir = sharks[i]
        peromons[sx][sy] = [i, k]

def discount_peromon(peromons):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if peromons[i][j][0] != 0:
                peromons[i][j][1] -= 1
                
                if peromons[i][j][1] == 0:
                    peromons[i][j][0] = 0

def count_sharks(sharks):
    count = 0
    for shark in sharks:
        if shark != None:
            count += 1
    return count

diffuse_peromon(peromons, sharks)

t = 0
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
            now_dir = shark_directions[i][sdir][j]
            nx, ny = sx + dir[now_dir][0], sy + dir[now_dir][1]
            
            if 0 < nx <= n and 0 < ny <= n and peromons[nx][ny][0] == 0:
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
                now_dir = shark_directions[i][sdir][j]
                nx, ny = sx + dir[now_dir][0], sy + dir[now_dir][1]
                
                if 0 < nx <= n and 0 < ny <= n and peromons[nx][ny][0] == i:
                    board[sx][sy] = 0
                    board[nx][ny] = i
                    sharks[i] = [nx, ny, now_dir]
                    break
    
    discount_peromon(peromons)
    diffuse_peromon(peromons, sharks)
    t += 1