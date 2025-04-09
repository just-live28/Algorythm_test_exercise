n, k = map(int, input().split())

# 조합: 값 채우기가 안쪽 loop, 코인 분배가 바깥 loop
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()

d = [0] * (k+1)
d[0] = 1
for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            d[i] += d[i-coin]

print(d[k])