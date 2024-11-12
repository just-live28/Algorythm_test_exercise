INF= int(1e9)

dp = [INF] * 30001
dp[1] = 0

x = int(input())

for i in range(2, x+1):
    dp[i] = min(dp[i], dp[i-1] + 1)
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])