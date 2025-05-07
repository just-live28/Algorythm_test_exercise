n = int(input())

d = [[[0] * 1024 for _ in range(10)] for _ in range(n+1)]
for i in range(1, 10):
    d[1][i][1 << i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(1024):
            if j > 0:
                d[i][j][k | (1 << j)] += (d[i-1][j-1][k] % int(1e9))
            if j < 9:
                d[i][j][k | (1 << j)] += (d[i-1][j+1][k] % int(1e9))

print(sum(d[n][j][1023] for j in range(10)) % int(1e9))