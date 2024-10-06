n, m = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

INF = int(1e9)
d = [INF] * 10001

d[m] = 0

def dfs(n):
    if n == 0:
        return
    
    for coin in coins:
        if n - coin < 0:
            continue
        
        d[n-coin] = min(d[n-coin], d[n] + 1)
        dfs(n-coin)

dfs(m)

if d[0] == INF:
    print(-1)
else:
    print(d[0])