n = int(input())
coins = list(map(int, input().split()))
m = int(input())

d = [0] * (m+1)
# 초깃값
for coin in coins:
    d[coin] = 1

for coin in coins:
    for i in range(m+1):
        if i - coin >= 0:
            d[i] += d[i-coin]

print(d)