import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k+1)

for i in range(1, n+1):
    w, v = map(int, input().split())
    
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[k])