import sys
input = sys.stdin.readline

t = int(input())

max_golds = []
for _ in range(t):
    # n 행 m 열
    n, m = map(int, input().split())

    board = [[0] * (m+1) for _ in range(n+1)]
    result = [[0] * (m+1) for _ in range(n+1)]

    line = list(map(int, input().split()))
    for a in range(1, n+1):
        row = line[(a-1)*m:a*m]
        for b in range(1, m+1):
            if b == 1:
                result[a][b] = row[b-1]
            board[a][b] = row[b-1]

    da = [-1, 0, 1]
    for b in range(1, m):
        for a in range(1, n+1):
            for i in da:
                na = a + i
                if na == 0 or na > n:
                    continue
                cost = result[a][b] + board[na][b+1]
                if cost > result[na][b+1]:
                    result[na][b+1] = cost
    max_gold = 0
    for a in range(1, n+1):
        if result[a][-1] > max_gold:
            max_gold = result[a][-1]

    max_golds.append(max_gold)

for i in max_golds:
    print(i)
        



        


