import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

result = []
for _ in range(t):
    n = int(input())

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    distance = [[INF]*n for _ in range(n)]

    distance[0][0] = board[0][0]

    q = []
    heapq.heappush(q, (distance[0][0], 0, 0))

    while q:
        dist, x, y = heapq.heappop(q)
            
        if dist > distance[x][y]:
            continue
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
                
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + board[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    result.append(distance[n-1][n-1])

for i in result:
    print(i)