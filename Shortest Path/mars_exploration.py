import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

t = int(input())

result = []
for _ in range(t):
    # n 공간 크기 n x n
    n = int(input())

    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))

    graph = [[INF] * n for _ in range(n)]

    graph[0][0] = board[0][0]

    da = [0,0,-1,1]
    db = [-1,1,0,0]

    q = []
    heapq.heappush(q, (board[0][0], 0, 0))
    while q:
        dist, a, b = heapq.heappop(q)
        if dist > graph[a][b]:
            continue
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            if na < 0 or nb < 0 or na > n-1 or nb > n-1:
                continue
            cost = dist + board[na][nb]
            if cost < graph[na][nb]:
                graph[na][nb] = cost
                heapq.heappush(q, (cost, na, nb))
                        
    result.append(graph[n-1][n-1])

for i in result:
    print(i)