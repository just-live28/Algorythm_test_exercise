from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = []
for _ in range(n):
    board.append([int(x) for x in input()])

def count_complex(x, y):
    count = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and not visited[nx][ny]:
                count += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    
    return count        

visited = [[False] * n for _ in range(n)]
total_complex = 0
complexes = []
for a in range(n):
    for b in range(n):
        if board[a][b] == 1 and not visited[a][b]:
            total_complex += 1
            visited[a][b] = True
            complexes.append(count_complex(a, b))

print(total_complex)
complexes.sort()
for cmp in complexes:
    print(cmp)