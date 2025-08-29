t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    line = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(line[m*i : m*(i+1)])

    d = [[0] * m for _ in range(n)]
    for i in range(n):
        d[i][0] = arr[i][0]

    for j in range(1, m):
        for i in range(n):
            left_top = left_bot = 0
            
            if i > 0:
                left_top = d[i-1][j-1]
            
            if i < n-1:
                left_bot = d[i+1][j-1]
            
            d[i][j] = max(d[i][j-1], left_top, left_bot) + arr[i][j]

    max_gold = 0
    for i in range(n):
        max_gold = max(max_gold, d[i][m-1])
    print(max_gold)