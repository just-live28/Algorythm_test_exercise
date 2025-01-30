n, m, k = map(int, input().split())

sharks = [[] for _ in range(m+1)]
board = []
peromon = [[[0] * 2 for _ in range(n)] for _ in range(n)] 
primary_dir = [[] for _ in range(m+1)]

dx = [None, -1, 1, 0, 0]
dy = [None, 0, 0, -1, 1]

for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(n):
        if line[j] != 0:
            sharks[line[j]] = [-1, i ,j]

init_dir = list(map(int, input().split()))            
for i in range(1, m+1):
    sharks[i][0] = init_dir[i-1]

for i in range(1, m+1):
    for _ in range(4):
        primary_dir[i].append(list(map(int, input().split())))

def count_shark(sharks):
    count = 0
    for i in range(1, m+1):
        if sharks[i] != None:
            count += 1
    return count

def diffuse_peromon(peromon, sharks, k):
    for i in range(1, m+1):
        if sharks[i] == None:
            continue
        s_num, sx, sy  = sharks[i]
        peromon[sx][sy] = [s_num, k]

def minus_permon(peromon):
    for x in range(n):
        for y in range(m):
            each = peromon[x][y]
            if each[0] != 0:
                each[1] -= 1
                if each[1] == 0:
                    each[0] = 0

def move_shark(sharks):
    now_sharks_moved = {}
    
    for i in range(1, m+1):
        if sharks[i] == None:
            continue
        s_dir, sx, sy = sharks[i]
        moved = False
        for j in primary_dir[i][s_dir - 1]:
            nx, ny = sx + dx[j], sy + dy[j]
            if 0 <= nx < n and 0 <= ny < n and peromon[nx][ny][0] == 0:
                moved = True
                if (nx, ny) not in now_sharks_moved:
                    now_sharks_moved[(nx, ny)] = [(i, j)]
                else:
                    now_sharks_moved[(nx, ny)].append((i, j))
                break
        if not moved:
            for j in primary_dir[i][s_dir - 1]:
                nx, ny = sx + dx[j], sy + dy[j]
                if 0 <= nx < n and 0 <= ny < n and peromon[nx][ny][0] == i:
                    sharks[i] = [j, nx, ny]
                    board[sx][sy] = 0
                    board[nx][ny] = i
                    break
    
    for x, y in now_sharks_moved.keys():
        if len(now_sharks_moved[(x, y)]) == 1:
            s_num, s_dir = now_sharks_moved[(x, y)][0]
            _, prev_x, prev_y = sharks[s_num]
            sharks[s_num] = [s_dir, x, y]
            board[prev_x][prev_y] = 0
            board[x][y] = s_num
        else:
            now_sharks_moved[(x, y)].sort()
            s_num, s_dir = now_sharks_moved[(x, y)][0]
            _, prev_x, prev_y = sharks[s_num]
            sharks[s_num] = [s_dir, x, y]
            board[prev_x][prev_y] = 0
            board[x][y] = s_num
            
            for s_num, s_dir in now_sharks_moved[(x, y)][1:]:
                _, prev_x, prev_y = sharks[s_num]
                board[prev_x][prev_y] = 0
                sharks[s_num] = None

diffuse_peromon(peromon, sharks, k)

result = 0
while True:
    print(count_shark(sharks))
    if count_shark(sharks) == 1:
        break
    
    if result > 1000:
        result = -1
        break
    
    move_shark(sharks)
    minus_permon(peromon)
    diffuse_peromon(peromon, sharks, k)
    
    result += 1

print(result)