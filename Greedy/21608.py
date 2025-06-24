n = int(input())
likes = [[] for _ in range(n * n + 1)]
orders = []
for _ in range(n * n):
    line = list(map(int, input().split()))
    orders.append(line[0])
    likes[line[0]].extend(line[1:])

board = [[0] * (n+1) for _ in range(n+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_place(target):
    candidate = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] == 0:
                like_count = 0
                space_count = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 1 <= nx <= n and 1 <= ny <= n:
                        if board[nx][ny] in likes[target]:
                            like_count += 1
                        elif board[nx][ny] == 0:
                            space_count += 1
                candidate.append((like_count, space_count, i, j))
    candidate.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    return candidate[0][2], candidate[0][3]

def cal_satisfaction():
    result = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            like = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 1 <= nx <= n and 1 <= ny <= n:
                    if board[nx][ny] in likes[board[i][j]]:
                        like += 1
            if like > 0:
                result += 10 ** (like-1)
    
    return result


for order in orders:
    tx, ty = find_place(order)
    board[tx][ty] = order

print(cal_satisfaction())