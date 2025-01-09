from collections import deque

n, l, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def organize_union(a, b, visited):
    q = deque()
    q.append((a, b))
    
    visited[a][b] = True
    
    union = []
    union.append((a, b))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(board[nx][ny] - board[x][y]) <= r and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    q.append((nx, ny))
    return union
    
def make_unions():
    visited = [[False] * n for _ in range(n)]
    unions = []
    
    for a in range(n):
        for b in range(n):
            if visited[a][b] == False:
                unions.append(organize_union(a, b, visited))
    return unions

def move_from_unions(unions):
    for union in unions:
        if len(union) == 1:
            continue
        
        total = 0
        for cx, cy in union:
            total += board[cx][cy]
        each_people = total // len(union)
        
        for cx, cy in union:
            board[cx][cy] = each_people
        
count = 0
while True:
    unions = make_unions()
    
    if len(unions) == n * n:
        break
    
    move_from_unions(unions)
    count += 1

print(count)