n, k = map(int, input().split())
weights = []
values = []
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

d = [[0] * (k+1) for _ in range(n+1)]
for i in range(n):
    for j in range(1, k+1):
        if i - 1 >= 0:
            d[i][j] = d[i-1][j]
        
        if j - weights[i] >= 0:
            if i - 1 >= 0:
                d[i][j] = max(d[i][j], d[i-1][j - weights[i]] + values[i])
            else:
                d[i][j] = values[i]

print(d[n-1][k])