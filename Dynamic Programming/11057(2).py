n = int(input())

d = [[0] * 10 for _ in range(n+1)]
for i in range(10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        count = 0
        for k in range(j+1):
            count += d[i-1][k] % 10007
        d[i][j] = count % 10007

print(sum(d[n]) % 10007)