import heapq
INF = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(input())
for _ in range(tc):
    N = int(input())

    board= []
    for _ in range(N):
        board.append(list(map(int, input().split())))
        
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = board[0][0]

    q = []
    heapq.heappush(q, (distance[0][0], (0, 0)))
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now[0]][now[1]]:
            continue
        
        for i in range(4):
            nx, ny = now[0] + dx[i], now[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + board[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))

    print(distance[N-1][N-1])