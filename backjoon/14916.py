INF = int(1e9)
n = int(input())
coins = [2, 5]

d = [INF] * 100001
d[2], d[5] = 1, 1
for i in range(1, n+1):
    if i - 2 >= 0:
        d[i] = min(d[i], d[i-2] + 1)
    if i - 5 >= 0:
        d[i] = min(d[i], d[i-5] + 1)

if d[n] == INF:
    print(-1)
else:
    print(d[n])