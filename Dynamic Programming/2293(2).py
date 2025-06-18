# 각 동전은 몇 개라도 사용할 수 있는데, 순서만 다른 것은 같은 것(조합)
# d[i]: i원을 만드는 모든 경우의 수
# for coin in coins 안에 for i 문
# d[i] += d[i-coin] (i-coin >= 0)
# d[0] = 1

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

d = [0] * (k+1)
d[0] = 1

for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            d[i] += d[i-coin]

print(d[k])