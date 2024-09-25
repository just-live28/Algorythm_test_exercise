import sys
import heapq
from collections import deque
input = sys.stdin.readline

# 보드 크기
n = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
# 사과 개수
k = int(input())
# 사과 좌표 입력(사과는 2의 값)
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 2
# 방향전환 횟수
l = int(input())
# 방향 전환 정보 입력
plans = []
for _ in range(l):
    t, d = input().split()
    heapq.heappush(plans, (int(t), d))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x, y, dir = 1, 1, 3
# directions[현재방향][L인지(0) D인지(1)]
directions = [(2, 3), (3, 2), (1, 0), (0, 1)]

time = 0
body = deque()
while(True):
    time += 1
    # 앞으로 한 칸 이동
    nx, ny = x + dx[dir], y + dy[dir]
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 1:
        #사과가 있다면 사과를 먹고 꼬리를 유지
        if board[nx][ny] == 2:
            board[nx][ny] = 1
            body.append((x, y))
            
            x, y = nx, ny
        #사과가 없다면 꼬리를 비워준다
        else:
            board[nx][ny] = 1
            body.append((x, y))
            
            bx, by = body.popleft()
            board[bx][by] = 0
            
            x, y = nx, ny
    else:
        break
    #plan이 존재할 때 정해진 시간에 도달하면 방향 전환
    if len(plans) > 0:
        if plans[0][0] == time:
            next_dir = heapq.heappop(plans)[1]
            if next_dir == 'L':
                dir = directions[dir][0]
            else:
                dir = directions[dir][1]
            
print(time)