n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i, n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i] + 1)
            
print(max(dp))