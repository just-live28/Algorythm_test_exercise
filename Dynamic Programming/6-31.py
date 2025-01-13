tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    mines = list(map(int, input().split()))

    d = []
    for i in range(len(mines) // m):
        d.append(mines[i*m:(i+1)*m])

    for y in range(1, m):
        for x in range(n):
            if x == 0:
                left_top = 0
            else:
                left_top = d[x-1][y-1]
            
            if x == n-1:
                left_bottom = 0
            else:
                left_bottom = d[x+1][y-1]
            
            d[x][y] = d[x][y] + max(left_top, d[x][y-1], left_bottom)

    print(max([x[-1] for x in d]))