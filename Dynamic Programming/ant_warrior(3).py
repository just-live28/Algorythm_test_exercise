# d[n] = max(arr[n] + d[n-2], d[n-1])

n = int(input())
array = list(map(int, input().split()))

dp = [0] * 101

dp[1] = array[0]
dp[2] = max(array[0], array[1])

for i in range(3, n+1):
    dp[i] = max(array[i-1] + dp[i-2], dp[i-1])

print(max(dp))