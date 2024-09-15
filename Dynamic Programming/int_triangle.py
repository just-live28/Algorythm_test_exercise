import sys
input = sys.stdin.readline

n = int(input())

dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for a in range(1, n):
    for b in range(a+1):
        if b-1 < 0:
            up_left = 0
        else:
            up_left = dp[a-1][b-1]
        
        if b >= a:
            up_right = 0
        else:
            up_right = dp[a-1][b]
        
        dp[a][b] = max(up_left + dp[a][b], up_right + dp[a][b])

print(max(dp[n-1]))