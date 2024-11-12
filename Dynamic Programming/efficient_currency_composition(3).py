import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
    
d = [INF] * 10001
d[m] = 0

for i in range(m, -1, -1):
    for coin in coins:
        if i + coin >= 0:
            d[i] = min(d[i], d[i + coin] + 1)

if d[0] == INF:
    print(-1)
else:
    print(d[0])