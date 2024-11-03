from collections import deque

n, l, r = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def make_unions(board):
    unions = []
    
    visited = [[False]*n for _ in range(n)]
    
    for a in range(n):
        for b in range(n):
            if visited[a][b] == False:
                union = []
                union.append((a, b))
                visited[a][b] = True
                
                q = deque()
                q.append((a, b))
                
                while q:
                    x, y = q.popleft()
                    
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        
                        if 0 <= nx < n and 0 <= ny < n:
                            difference = abs(board[x][y] - board[nx][ny])
                            if l <= difference <= r:
                                if visited[nx][ny] == False:
                                    visited[nx][ny]  = True
                                    union.append((nx, ny))
                                    q.append((nx, ny))
                
                unions.append(union)
    
    return unions

count = 0
while True:
    unions = make_unions(board)
    
    if len(unions) == n * n:
        break
    
    for union in unions:
        if len(union) == 1:
            continue
        
        total_people = 0
        for ux, uy in union:
            total_people += board[ux][uy]
        
        average_people = total_people // len(union)
        
        for ux, uy in union:
            board[ux][uy] = average_people
    
    count += 1

print(count)