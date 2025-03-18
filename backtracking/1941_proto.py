# board = []
# for _ in range(5):
#     board.append(input())
    
# visited = [[False] * 5 for _ in range(5)]
# result = [None] * 7
# count = 0

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def func(k, x, y):
#     global count
#     if k == 7:
#         q = deque()
#         q.append((x, y))
#         count_s = 0
#         count_y = 0
#         while q:
#             now_x, now_y = q.popleft()
#             if board[now_x][now_y] == 'S':
#                 count_s += 1
#             else:
#                 count_y += 1
            
#             for i in range(4):
#                 nx, ny = now_x + dx[i], now_y + dy[i]
#                 if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny]:
#                     q.append((nx, ny))
        
#         if count_s + count_y == 7 and count_s >= 4:
#             count += 1            
#         return
    
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
#             visited[nx][ny] = True
#             result[k] = board[nx][ny]
#             func(k+1, nx, ny)
#             visited[nx][ny] = False

# for i in range(5):
#     for j in range(5):
#         visited[i][j] = True
#         result[0] = board[i][j]
#         func(1, i, j)
#         visited[i][j] = False

# print(count)
from collections import deque
from itertools import combinations

board = []
students = []
for i in range(5):
    board.append(input())
    for j in range(5):
        students.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_seven_princess(sevens):
    q = deque()
    q.append(sevens[0])
    total = 1
    som = 1 if board[sevens[0][0]][sevens[0][1]] == 'S' else 0
    visited = [sevens[0]]
    while q:
        sx, sy = q.popleft()
        for i in range(4):
            nx, ny = sx + dx[i], sy + dy[i]
            if (nx, ny) in sevens and (nx, ny) not in visited:
                visited.append((nx, ny))
                q.append((nx, ny))
                total += 1
                if board[nx][ny] == 'S':
                    som += 1
    if total == 7 and som >= 4:
        return True
    return False

count = 0
for sevens in combinations(students, 7):
    if is_seven_princess(sevens):
        count += 1
print(count)