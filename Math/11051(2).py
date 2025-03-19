# n이 1~1000
# 0 <= k <= n

# n C k = n-1 C k + n-1 C k-1

n, k = map(int, input().split())
dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    dp[i][0], dp[i][i] = 1, 1
    for j in range(1, n+1):
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 10007

print(dp[n][k])