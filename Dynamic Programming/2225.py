n, k = map(int, input().split())

d = [[0] * (k+1) for _ in range(n+1)]
d[0][0] = 1

for n in range(1, n+1):
    for c in range(1, k+1):
        for i in range(n+1):
            if n >= i:
                d[n][c] += d[n-i][c-1]
            else:
                break

print(sum(d[n]) % 1000000000)