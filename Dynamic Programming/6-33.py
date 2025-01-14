n = int(input())

times = [0] * (n+1)
pays = [0] * (n+1)

for i in range(1, n+1):
    t, p = map(int, input().split())
    times[i] = t
    pays[i] = p

d = [0] * (n+2)

max_earn = 0
for i in range(n, 0, -1):
    if i + times[i] -1 <= n:
        d[i] = max(pays[i] + d[i + times[i]], max_earn)
        max_earn = max(max_earn, d[i])
    else:
        d[i] = max_earn

print(d[1])