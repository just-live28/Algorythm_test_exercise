from collections import deque

n, m = map(int, input().split())

board = [[None]*m for _ in range(n)]
for a in range(n):
    line = input()
    for b in range(m):
        board[a][b] = line[b]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

right_start_visited = [[-1]*m for _ in range(n)]
q = deque()
q.append((board[0][0], 0, 0))
right_start_visited[0][0] = 0

while q:
    color, x, y = q.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and right_start_visited[nx][ny] == -1:
            if color == board[nx][ny]:
                right_start_visited[nx][ny] = 1
            else:
                right_start_visited[nx][ny] = 0
            
            if color == 'W':
                q.append(('B', nx, ny))
            else:
                q.append(('W', nx, ny))

wrong_start_visited = [[-1]*m for _ in range(n)]
q2 = deque()
wrong_start_visited[0][0] = 1
if board[0][0] == 'W':
    q2.append(('B', 0, 0))
else:
    q2.append(('W', 0, 0))
    
while q2:
    color, x, y = q2.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and wrong_start_visited[nx][ny] == -1:
            if color == board[nx][ny]:
                wrong_start_visited[nx][ny] = 1
            else:
                wrong_start_visited[nx][ny] = 0
            
            if color == 'W':
                q2.append(('B', nx, ny))
            else:
                q2.append(('W', nx, ny))

def count_change_spaces(x, y):
    count1 = 0
    count2 = 0
    for a in range(x, x+8):
        for b in range(y, y+8):
            if right_start_visited[a][b] == 1:
                count1 += 1
            elif wrong_start_visited[a][b] == 1:
                count2 += 1
    return min(count1, count2)

min_count = int(1e9)
for a in range(n - 8 + 1):
    for b in range(m - 8 + 1):
        min_count = min(min_count, count_change_spaces(a, b))

print(min_count)