# n, m

# m은 열
# d[1] 은 
# d[m] = max(left_top, left_mid, left_bottom)

t = int(input())

results = []
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    board = []
    for i in range(n):
        board.append(array[i * m: (i+1) * m])

    d = [[0]*m for _ in range(n)]

    for a in range(n):
        d[a][0] = board[a][0]

    for b in range(1, m):
        for a in range(n):    
            if a - 1 < 0:
                left_top = 0
            else:
                left_top = d[a-1][b-1]
            
            left_mid = d[a][b-1]
            
            if a + 1 >= n:
                left_bottom = 0
            else:
                left_bottom = d[a+1][b-1]
            
            d[a][b] = max(left_top + board[a][b], left_mid + board[a][b], left_bottom + board[a][b])
    
    max_gold = 0
    for a in range(n):
        max_gold = max(max_gold, d[a][-1])

    results.append(max_gold)

for result in results:
    print(result)