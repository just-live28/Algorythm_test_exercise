# n 동전 종류 m 만들 값
n, m = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

d = [10001] * 10001
for coin in coins:
    d[coin] = 1

for i in range(1, m+1):
    for coin in coins:
        if not i - coin > 0 or d[i - coin] > 10000:
            continue
        d[i] = min(d[i], d[i - coin] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])