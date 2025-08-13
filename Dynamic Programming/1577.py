n, m = map(int, input().split())
k = int(input())
weak_roads = set()
for _ in range(k):
    a, b, c, d = map(int, input().split())
    weak_roads.add((a, b , c, d))

d = [[0] * (m+1) for _ in range(n+1)]
d[0][0] = 1
for i in range(n+1):
    for j in range(m+1):
        if i == 0 and j == 0:
            continue
        
        from_left = from_bottom = 0
        if 0 <= j-1 <= m and ((i, j-1, i, j) not in weak_roads and (i, j, i, j-1) not in weak_roads):
            from_left = d[i][j-1]
        if 0 <= i-1 <= n and ((i-1, j, i, j) not in weak_roads and (i, j, i-1, j) not in weak_roads):
            from_bottom = d[i-1][j]
    
        d[i][j] = from_left + from_bottom

print(d[n][m])