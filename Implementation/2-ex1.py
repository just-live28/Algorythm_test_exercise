n = int(input())
plans = list(input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
directions = ['L', 'R', 'U', 'D']

x, y = 1, 1
for plan in plans:
    for i in range(len(directions)):
        if plan == directions[i]:
            nx, ny = x + dx[i], y + dy[i]
    
    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny

print(x, y)