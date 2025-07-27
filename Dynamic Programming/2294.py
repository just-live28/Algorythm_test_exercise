# n가지 종류의 동전, 합 k, 최소 동전, 중복 가능
# d[i] : i원일 때, 최소 동전 갯수
# d[i] = min(d[i], d[i-coin] + 1) (단, i-coin >= 0)
# d[0] = 1
INF = int(1e9)

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

d = [INF] * (k+1)
d[0] = 0

for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            d[i] = min(d[i], d[i-coin] + 1)

if d[k] == INF:
    print(-1)
else:
    print(d[k])