INF = int(1e9)

n, k = map(int, input().split())

d = [INF] * 100001
d[0] = 0
coins = []
for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    d[coin] = 1

for i in range(1, k+1):
    for coin in coins:
        if i - coin >= 0:
            d[i] = min(d[i], d[i-coin] + 1)

if d[k] == INF:
    print(-1)
else:
    print(d[k])