n, k = map(int, input().split())

d = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(k+1):
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j - w] + v)

print(max(d[n]))