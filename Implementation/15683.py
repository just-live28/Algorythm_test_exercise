n, m = map(int, input().split())
board = []
cameras = []
for a in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for b in range(m):
        if 1 <= line[b] <= 5:
            cameras.append((line[b], a, b))

dir = [0, [[0], [1], [2], [3]], [[0,1],[2,3]], [[0,3],[0,2],[1,3],[1,2]], [[0,1,2], [0,1,3], [0,2,3], [1,2,3]], [[0,1,2,3]]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_bline_spot(board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1
    return count

def surveillance_on(board, cx, cy, directions):
    changed = []
    for d in directions:
        nx, ny = cx + dx[d], cy + dy[d]
        while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 6:
            if board[nx][ny] == 0:
                board[nx][ny] = '#'
                changed.append((nx, ny))
            nx += dx[d]
            ny += dy[d]
    return changed

def surveillance_off(board, changed):
    for cx, cy in changed:
        board[cx][cy] = 0

min_blined_spot = m * n - len(cameras)
def func(k):
    global min_blined_spot
    if k == len(cameras):
        min_blined_spot = min(min_blined_spot, count_bline_spot(board))
        return
    
    ctype, cx, cy = cameras[k]
    for each in dir[ctype]:
        changed = surveillance_on(board, cx, cy, each)
        func(k+1)
        surveillance_off(board, changed)

func(0)
print(min_blined_spot)