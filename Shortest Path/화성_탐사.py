# 양방향 연결 (모든 좌표에 대해)
# board는 0-sided / 간선의 경우, for 문에서 dx,dy로 처리 / 0, 0 출발
import heapq
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = board[0][0]

    q = []
    heapq.heappush(q, (board[0][0], 0, 0))
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

    print(distance[n-1][n-1])