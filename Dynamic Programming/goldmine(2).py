from collections import deque

results = []

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    lines = list(map(int, input().split()))

    board = [[0] * (m+1) for _ in range(n+1)]

    for a in range(1, n+1):
        line = lines[(a-1)*m:a*m]
        for b in range(1, m+1):
            board[a][b] = line[b-1]

    result = []
    for a in range(1, n+1):
        d = [[0] * (m+1) for _ in range(n+1)]
        d[a][1] = board[a][1]
        
        q = deque()
        q.append((a,1))
        
        while q:
            x, y = q.popleft()
            
            if y == m:
                break
            
            up, mid, down = 0, 0, 0
            if 1 <= x-1 <= n:
                up = board[x-1][y+1]
            if 1 <= x+1 <= n:
                down = board[x+1][y+1]
            mid = board[x][y+1]
            
            if max(up, mid, down) == up:
                d[x-1][y+1] = d[x][y] + up
                q.append((x-1, y+1))
            elif max(up, mid, down) == down:
                d[x+1][y+1] = d[x][y] + down
                q.append((x+1, y+1))
            else:
                d[x][y+1] = d[x][y] + mid
                q.append((x, y+1))
        
        max_gold = 0
        for a in range(1, n+1):
            if d[a][-1] > max_gold:
                max_gold = d[a][-1]
        
        result.append(max_gold)

    results.append(max(result))

for result in results:
    print(result)