from collections import deque

n, l, r = map(int, input().split())

board = [[0] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    line = list(map(int, input().split()))
    for b in range(1, n+1):
        board[a][b] = line[b-1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    people = board[a][b]
    union = [(a, b)]
    
    united[a][b] = True
    q = deque()
    q.append((a, b))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 1 <= nx and nx <= n and 1 <= ny and ny <= n and not united[nx][ny]:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    union.append((nx, ny))
                    people += board[nx][ny]
                    united[nx][ny] = True
                    q.append((nx, ny))
    
    return union, people // len(union)

result = 0
while(True):
    # united : 방문했는지 여부
    united = [[False] * (n+1) for _ in range(n+1)]
    
    is_moved = False
    for a in range(1, n+1):
        for b in range(1, n+1):
            if united[a][b] == False:
                union, people = bfs(a, b)
                
                if len(union) > 1:
                    is_moved = True
                    for x, y in union:
                        board[x][y] = people
    
    if not is_moved:
        break
    
    result += 1

print(result)